#!/usr/bin/env python

import sys
import traceback

import tornado.ioloop
import tornado.web
import tornado.gen
import json
from collections import defaultdict

from settings import SEARCH_PARAMS, SERVER_PARAMS

sys.path.append("../..")


from api.searcher import perform_search


class Finder(tornado.web.RequestHandler):
    """    Request dispatcher
    """
    @tornado.web.asynchronous
    def get(self, *args):
        # resp = SERVER_PARAMS['not_found_request']
        # indexes to search
        search_where_dict = {
            'stage': ["project_rt", "task_rt", "task_comment_rt"],
            'prod': ["project_prod_rt", "task_prod_rt", "task_comment_prod_rt"]
        }
        search_results = {}

        try:
            # search_where_lst = self.request.arguments.get('index', ('*',))
            proj_ids_list = [int(v) for v in self.request.arguments.get('proj', [''])[0].split(',') if v]
            phrase_for_search_lst = self.request.arguments.get('word', [])
            search_where_lst = search_where_dict.get(
                self.request.arguments.get('where', ['stage'])[0], search_where_dict['stage']
            )

            if phrase_for_search_lst:
                phrase_for_search = phrase_for_search_lst[0]

                for search_where in search_where_lst:
                    resp = perform_search(
                        phrase_for_search, search_where, SEARCH_PARAMS['host'],
                        SEARCH_PARAMS['port'], proj_ids_list
                    )

                    if isinstance(resp, list):
                        search_results[search_where.replace('_rt', '')] = [int(id) for id in resp]

        except Exception as e:
            search_results = SERVER_PARAMS['system_error_message'].format(e.message, traceback.format_exc())

        self.finish(json.dumps(search_results))
        # self.finish(resp)


application = tornado.web.Application([
    tornado.web.url('/find/(.*)', Finder),
])

if __name__ == '__main__':
    print "Search Server started. port: {}".format(SERVER_PARAMS['port'])
    application.listen(SERVER_PARAMS['port'])
    tornado.ioloop.IOLoop.instance().start()

