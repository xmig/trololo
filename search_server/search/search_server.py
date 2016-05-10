#!/usr/bin/env python

import sys
import traceback

import tornado.ioloop
import tornado.web
import tornado.gen
import json

from settings import SEARCH_PARAMS, SERVER_PARAMS

sys.path.append("../..")


from api.searcher import perform_search


class Finder(tornado.web.RequestHandler):
    """    Request dispatcher
    """
    @tornado.web.asynchronous
    def get(self, *args):
        # resp = SERVER_PARAMS['not_found_request']
        try:
            # search_where_lst = self.request.arguments.get('index', ('*',))
            search_where_lst = ["project_rt", "task_rt", "task_comment_rt"]
            phrase_for_search_lst = self.request.arguments.get('word', None)
            if phrase_for_search_lst and len(phrase_for_search_lst) > 0:
                phrase_for_search = phrase_for_search_lst[0]
                search_where = search_where_lst[0]

            # phrase_for_search = "test"
            # search_where = "*"
            resp = perform_search(
                phrase_for_search, search_where, SEARCH_PARAMS['host'], SEARCH_PARAMS['port']
            )
        except Exception as e:
            resp = SERVER_PARAMS['system_error_message'].format(e.message, traceback.format_exc())
        if isinstance(resp, list):
            resp = [int(id) for id in resp]

        self.finish(json.dumps(resp))
        # self.finish(resp)


application = tornado.web.Application([
    tornado.web.url('/find/(.*)', Finder),
])

if __name__ == '__main__':
    print "Search Server started. port: {}".format(SERVER_PARAMS['port'])
    application.listen(SERVER_PARAMS['port'])
    tornado.ioloop.IOLoop.instance().start()

