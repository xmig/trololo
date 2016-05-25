'use strict';

angular.module('userApp').factory('commentService', function($resource, $cookies) {
    return $resource("/projects/comments/", null,
        { 'get':    {method:'GET'},
          'getAll': {method:'GET', params: {'page_size': 0}, isArray:true},
          'save':   {method:'POST', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'create': {method:'POST', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'update': {method:'PUT',  data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});



angular.module('userApp').factory('taskCommentService', function($resource, $cookies) {
    return $resource("/tasks/comments/", null,
        { 'get':    {method:'GET'},
          'save':   {method:'POST', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'create': {method:'POST', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'update': {method:'PUT',  data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});