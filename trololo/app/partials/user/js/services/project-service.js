'use strict';

angular.module('userApp').factory('projectService', function($resource, $cookies) {
    return $resource("/projects/", null,
        { 'get':    {method:'GET'},
          'save':   {method:'POST'},
          'create': {method:'POST'},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});
