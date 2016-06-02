'use strict';

angular.module('userApp').factory('personalInfoService', function($resource, djangoAuth) {
    return $resource("/users/profile/", null,
        { 'get':    {method:'GET'},
          'save':   {method:'POST'},
          'create': {method:'POST'},
          'update': {
            method:'PUT', data: {}, headers: {'X-CSRFToken': djangoAuth.getCsrfToken}
          },
          'update_photo': {method:'PUT', data: {}, headers: {'X-CSRFToken': djangoAuth.getCsrfToken, 'Content-Type': undefined, transformRequest: angular.identity,}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});

angular.module('userApp').factory('usersService', function($resource, $cookies) {
    return $resource("/users/", null,
        {
            'get':    {method:'GET'}
        }
    );
});
