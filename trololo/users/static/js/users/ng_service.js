(function(angular){
    'use strict';

    angular.module("UserSettings", ["ngResource"]).
        factory('UserSettingsService', function($resource) {
            return $resource('/user/settings/:user', {}, {
                get: { method: 'GET' },
                update: { method: 'PUT',    params: {user: '@user'} },
                delete: { method: 'DELETE', params: {user: '@user'} },
                create: { method: 'POST',   params: {} }
            })
    });
//---------------------------------------------------------------------
        angular.module("User", ["ngResource"]).
        factory('UserService', function($resource) {
           return $resource('/users/api/users\/:id\/.', {}, {
                get:    { method: 'GET' ,   params: {id: '@id'}},
                update: { method: 'PUT',    params: {id: '@id'} },
                delete: { method: 'DELETE', params: {id: '@id'} },
                create: { method: 'POST'}
            })
    });

//---------------------------------------------------------------------
        angular.module("UserRole", ["ngResource"]).
        factory('UserRoleService', function($resource) {
           return $resource('/users/api/role\/:id\/.', {}, {
                get:    { method: 'GET' ,   params: {id: '@id'}},
                update: { method: 'PUT',    params: {id: '@id'} },
                delete: { method: 'DELETE', params: {id: '@id'} },
                create: { method: 'POST'}
            })
    });

//---------------------------------------------------------------------
        angular.module("PossibleRoles", ["ngResource"]).
        factory('PossibleRolesService', function($resource) {
           return $resource('/users/api/permission\/:id\/.', {}, {
                get:    { method: 'GET' ,   params: {id: '@id'}},
                update: { method: 'PUT',    params: {id: '@id'} },
                delete: { method: 'DELETE', params: {id: '@id'} },
                create: { method: 'POST'}
            })
    });

})(window.angular);

