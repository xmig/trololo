'use strict';

angular.module('userApp').factory('task_selectedService', function($resource, $cookies) {
    return $resource("/tasks\/:id\/.", {},
        { 'get':    {method:'GET', params: {id: '@id'}},
          'save':   {method:'POST', params: {id: '@id'}},
          'create': {method:'POST', params: {id: '@id'}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
          'query':  {method:'GET', isArray:true, params: {id: '@id'}},
          'delete': {method:'DELETE', params: {id: '@id'}}
        }
    );
});

angular.module('userApp').factory('task_tagService', function($resource, $cookies) {
    return $resource("/tasks\/:id\/tag\/:tag_name\/", {},
        { 'add_tag':    {method:'PUT', params: {id: '@id', tag_name: '@tag_name'}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'delete_tag': {method:'DELETE', params: {id: '@id', tag_name: '@tag_name'}}
        }
    );
});


//'use strict';
//
//angular.module('userApp').factory('taskService', function($resource, $cookies) {
//    return $resource("/tasks\/:id\/.", null,
//        { 'get':    {method:'GET', params: {id: '@id'}},
//          'save':   {method:'POST', params: {id: '@id'}},
//          'create': {method:'POST', params: {id: '@id'}},
//          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
//          'query':  {method:'GET', isArray:true, params: {id: '@id'}},
//          'delete': {method:'DELETE', params: {id: '@id'}}
//        }
//    );
//});