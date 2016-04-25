angular.module('userApp').controller('nutritionController', ['$mdEditDialog', '$q', '$scope', '$timeout', function ($mdEditDialog, $q, $scope, $timeout) {
    'use strict';

    $scope.selected = [];

    $scope.options = {
        autoSelect: true,
        boundaryLinks: false,
        largeEditDialog: false,
        pageSelector: false,
        rowSelection: true
    };

    $scope.query = {
        order: 'name',
        limit: 5,
        page: 1
    };

    $scope.loadStuff = function () {
        $scope.promise = $timeout(function () {
            // loading
        }, 2000);
    };

    $scope.logItem = function (item) {
        console.log(item.name, 'was selected');
    };

    $scope.logOrder = function (order) {
        console.log('order: ', order);
    };

    $scope.logPagination = function (page, limit) {
        console.log('page: ', page);
        console.log('limit: ', limit);
        
//        $scope.promise = $timeout(function () {
//        }, 2000);
    };
    
    
//    $scope.onReorder = function(order) {
//
//        console.log('Scope Order: ' + $scope.query.order);
//        console.log('Order: ' + order);
//    
//        $scope.promise = $timeout(function () {
//    
//        }, 2000);
//  };
    
    
    
}]);
