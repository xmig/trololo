'use strict';

angular.module('userApp').factory('commentSelectedService', function($resource, $cookies) {
    return $resource("/projects/comments\/:id\/.", {},
        { 'get':    {method:'GET', params: {id: '@id'}},
          'save':   {method:'POST', params: {id: '@id'}},
          'create': {method:'POST', params: {id: '@id'}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
          'query':  {method:'GET', isArray:true, params: {id: '@id'}},
          'put':    {method:'PUT', headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'remove_comment': {method: 'DELETE', headers: {'X-CSRFToken': $cookies.get('csrftoken')}}
        }
    );
});


angular.module('userApp').factory('taskCommentSelectedService', function($resource, $cookies) {
    return $resource("/tasks/comments\/:id\/.", {},
        { 'get':    {method:'GET', params: {id: '@id'}},
          'save':   {method:'POST', params: {id: '@id'}},
          'create': {method:'POST', params: {id: '@id'}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
          'query':  {method:'GET', isArray:true, params: {id: '@id'}},
//          'delete': {method:'DELETE', params: {id: '@id'}};
          'put':    {method:'PUT', headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'remove_comment_task': {method: 'DELETE', headers: {'X-CSRFToken': $cookies.get('csrftoken')}}
        }
    );
});