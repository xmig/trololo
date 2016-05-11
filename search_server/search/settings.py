
#from sphinxapi
SPH_MATCH_PHRASE = 2

SEARCH_PARAMS = {
    'mode':     SPH_MATCH_PHRASE,
    'host':     'localhost',
    'port':     10312,
    'index':    '*',
    'weights':  [10, 1],
}

SERVER_PARAMS = {
    'port': 8005,
    # 'port': 8555,
    'not_found_request':    "NOTHING WAS REQUESTED",
    'not_found_response':   "NOTHING FOUND FOR '{0}'",
    'system_error_message': "SEARCH IS TEMPORARY UNAVAILABLE {} {}",
}

