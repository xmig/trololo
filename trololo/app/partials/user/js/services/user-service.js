'use strict';

angular.module('userApp').factory('personalInfoService', function($resource, $cookies) {
    return $resource("/users/profile/", null,
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
