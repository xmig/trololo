'use strict';

angular.module('userApp').factory('projectSelectedService', function($resource, $cookies) {
    return $resource("/projects/:id",
        {
            id: '@id'
        },
        {
            'get':    {method:'GET'},
            'save':   {method:'POST'},
            'create': {method:'POST'},
            'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
            'query':  {method:'GET', isArray:true},
            'remove': {method:'DELETE'},
            'delete': {method:'DELETE'}
        }
    );
});

angular.module('userApp').factory('project_tagService', function($resource, $cookies) {
    return $resource("/projects\/:id\/tag\/:tag_name\/", {},
        { 'add_tag':    {method:'PUT', params: {id: '@id', tag_name: '@tag_name'}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'delete_tag': {method:'DELETE', params: {id: '@id', tag_name: '@tag_name'}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}}
        }
    );
});

angular.module('userApp').factory('projectStatusService', function($resource, $cookies) {
    return $resource("/status/", {},
        { 'add_status':    {method:'POST', headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'get': {method:'GET', params: {ordering: 'order_number'}},
          'get_all': {method: 'GET', params: {ordering: 'order_number'}, isArray:true}
        }
    );
});