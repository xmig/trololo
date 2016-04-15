'use strict';

angular.module('userApp').factory('userService', function($resource, $cookies) {
    return $resource("/users\/:id\/", null,
        { 'get':    {method:'GET', params: {id:'@id'}},
          'save':   {method:'POST'},
          'create': {method:'POST'},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'update_photo': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken'), 'Content-Type': undefined, transformRequest: angular.identity,}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});
