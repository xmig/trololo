'use strict';

angular.module('userApp').factory('searchService', function($resource, $cookies) {
    return $resource("/global_search/:search_phrase/",
        {id: '@search_phrase'},
        {
            'get': {method:'GET'},
        }
    );
});