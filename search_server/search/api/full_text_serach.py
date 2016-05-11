
class ISearchClient(object):
    """
    Search client interface
    """
    def search(self, words_for_search, where, mode):
        raise NotImplemented

