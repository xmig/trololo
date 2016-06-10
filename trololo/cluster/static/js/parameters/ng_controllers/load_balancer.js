(function (angular) {
    'use strict';
    parametersApp.controller('ClusterInfoService', function($scope, $http, $filter, ClusterInfoService ) {
    $scope.clusterInfo= ClusterInfoService.query(function(data) {
        console.log(data)
        });

    $scope.cluster_info_change = function(host){
        NProgress.start();
        var request = {
         method: 'POST',
         url: '/load_balancer/',
         data: {"host": host}
        };
        $http(request).then(function successCallback(response) {
            NProgress.done();
          }, function errorCallback(response) {
            NProgress.done();
          });
    }
    });

})(window.angular);

