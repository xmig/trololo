

from .sphinx.sphinx_search import SphinxSearchClient

__all__ = ["perform_search"]

def parse_search_respond(data):
    """
    data Example: {'status': 0, 'matches': [{'id': 1000003301, 'weight': 1, 'attrs': {'dbid': '5258271e1d41c85dd1a2f6d6'}},
    """
    result = []
    if data and data.get('status') == 0:
        matches = data.get('matches')
        for item in matches:
            result.append(str(item["id"]))
            # result.append(str(item['attrs']['dbid']))

    return result

def perform_search(phrase_for_search, index='*', host='localhost', port=10312, proj_ids_list=[]):
    """    Perform search itself
    """
    result = []

    if phrase_for_search:
        finder = SphinxSearchClient(host, port, proj_ids_list)
        data = finder.search(phrase_for_search, index)
        result.extend(parse_search_respond(data))
    return result
