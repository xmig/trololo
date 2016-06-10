'use strict';

angular.module('userApp').factory('clusterService', function($resource, $cookies) {
    return $resource("/system/cluster_info/api/cluster_info/", null,
        { 'get':    {method:'GET'},
          'save':   {method:'POST'},
          'create': {method:'POST', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'update': {method:'PUT', data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
          'query':  {method:'GET', isArray:true},
          'remove': {method:'DELETE'},
          'delete': {method:'DELETE'}
        }
    );
});

angular.module('userApp').factory('clusterInfoService', function ($resource, $cookies) {
    return $resource('/system/cluster_info/api/cluster_info\/:id\/', {},
    {
        'get':    { method: 'GET' ,   params: {id: '@id'}},
        'update': { method: 'PUT',    data: {}, headers: {'X-CSRFToken': $cookies.get('csrftoken')}, params: {id: '@id'}},
        'delete': {method: 'DELETE', headers: {'X-CSRFToken': $cookies.get('csrftoken')}},
        'create': { method: 'POST'}
    })
});


