(function (angular) {
    'use strict';
    parametersApp.factory('ClusterInfoService', function ($resource) {
        return $resource('/cluster_info/api/cluster_info\/:id\/.', {}, {
            get:    { method: 'GET' ,   params: {id: '@id'}},
            update: { method: 'PUT',    params: {id: '@id'} },
            delete: { method: 'DELETE', params: {id: '@id'} },
            create: { method: 'POST'}
        })
    });


})(window.angular);