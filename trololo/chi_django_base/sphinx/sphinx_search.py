"""
Search client based on Sphinx
"""

from sphinxapi_3883 import *


class ISearchClient(object):
    """
    Search client interface
    """
    def search(self, words_for_search, where, mode):
        raise NotImplemented


class SphinxSearchClient(ISearchClient):
    DEFAULT_WEIGHTS = [100, 1]

    def __init__(self, host, port, filters):
        self._client = SphinxClient()
        self._client.SetServer(host, port)

        for fltr in filters:
            if fltr:
                f_name, f_val = fltr.items()[0]
                self._client.SetFilter(f_name, f_val)
        self._client.SetWeights(self.DEFAULT_WEIGHTS)

    def search(self, words_for_search, where='*', mode=SPH_MATCH_EXTENDED2):
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

    print "OK {0}".format(item_id)
