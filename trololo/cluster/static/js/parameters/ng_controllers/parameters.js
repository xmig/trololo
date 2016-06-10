//(function (angular) {
//    'use strict';
//    parametersApp.controller('Parameters', ['$scope', 'parametersService', '$filter', 'PaginationService', 'TableService', function ($scope, parametersService, $filter, PaginationService, TableService) {
//        $scope.parametersData = parametersService.query();
//        //$scope.getRedirectForUpdate = function(id) {
//        //    change_location("/redirects/"+ id + "/");
//        //};
//        $scope.columns = [
//            {name:'Parameter Name', OrderedBy: "parameter_name"},
//            {name:'Value',          OrderedBy: "value"},
//            {name:'Description',    OrderedBy: "description"},
//            {name:'Enabled',        OrderedBy: "enabled"}
//        ];
//        $scope.parameters_add = function() {
//             change_location("/system/parameters/add/");
//        };
//        PaginationService.ng_pagginator_mixin($scope, $scope.parametersData);
//        TableService.ng_tableview_mixin($scope, $scope.parametersData, $filter);
//        //ng_pagginator_mixin($scope, $scope.parametersData);
//        //ng_tableview_mixin($scope, $scope.parametersData, $filter);
//        $scope.prepare_sorter_data();
//    }]);
//})(window.angular);




