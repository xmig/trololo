'use strict';

angular.module('userApp').factory('taskService', function($resource, djangoAuth) {
    return $resource("/tasks/", null,
        { 'get':    {method:'GET'},
          'save':   {method:'POST'},
          'create': {method:'POST', data: {}, headers: {'X-CSRFToken': djangoAuth.getCsrfToken}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': djangoAuth.getCsrfToken}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});