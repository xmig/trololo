'use strict';

angular.module('userApp').factory('activityListService', function($resource, $cookies) {
    return $resource("/activities/a/", null,
        { 'get':    {method:'GET'} }
    );
});
