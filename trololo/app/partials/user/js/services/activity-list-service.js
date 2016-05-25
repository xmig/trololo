'use strict';

angular.module('userApp').factory('activityListService', function($resource, $cookies) {
    return $resource("/activities/a/", null,
        {
            'get':    {method:'GET'},
            'getAll': {method:'GET', params: {'page_size': 0}, isArray:true}
        }
    );
});
