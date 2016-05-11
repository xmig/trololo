"""
Search client based on Sphinx
"""

from sphinxapi import *
from ..full_text_serach import ISearchClient


class SphinxSearchClient(ISearchClient):
    DEFAULT_WEIGHTS = [100, 1]

    def __init__(self, host, port, proj_ids_list):
        self._client = SphinxClient()
        self._client.SetServer(host, port)
        if proj_ids_list:
            self._client.SetFilter('project_id', proj_ids_list)
        self._client.SetWeights(self.DEFAULT_WEIGHTS)

    def search(self, words_for_search, where='*', mode=SPH_MATCH_EXTENDED):
        """
        Perform searching
        Returns result if only something was found
        """
        self._client.SetMatchMode(mode)
        res = self._client.Query(words_for_search, where.encode('utf-8'))
        return res


if __name__ == '__main__':
    search_client = SphinxSearchClient("127.0.0.1", 10312)
    item_id = search_client.search("test")

    print "OK {0}".format(id)
