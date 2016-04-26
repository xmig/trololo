'use strict';

angular.module('userApp').factory('commentSelectedService', function($resource, $cookies) {
    return $resource("/projects/comments\/:id\/.", {},
        { 'get':    {method:'GET', params: {id: '@id'}},
          'save':   {method:'POST', params: {id: '@id'}},
          'create': {method:'POST', params: {id: '@id'}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
          'query':  {method:'GET', isArray:true, params: {id: '@id'}},
          'delete': {method:'DELETE', params: {id: '@id'}}
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
          'delete': {method:'DELETE', params: {id: '@id'}}
        }
    );
});

//'use strict';
//
//angular.module('userApp').factory('commentSelectedService', function($resource, $cookies) {
//    return $resource("/projects/comments/:id",
//        {
//            id: '@id'
//        },
//        {
//            'get':    {method:'GET'},
//            'save':   {method:'POST'},
//            'create': {method:'POST'},
//            'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
//            'query':  {method:'GET', isArray:true},
//            'remove': {method:'DELETE'},
//            'delete': {method:'DELETE'}
//        }
//    );
//});