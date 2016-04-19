//angular.module('userApp').controller('nutritionController', ['$mdEditDialog', '$q', '$scope', '$timeout', function ($mdEditDialog, $q, $scope, $timeout) {
//    'use strict';

//    $scope.selected = [];
//
//    $scope.options = {
//        autoSelect: true,
//        boundaryLinks: false,
//        largeEditDialog: false,
//        pageSelector: false,
//        rowSelection: true
//    };
//
//    $scope.query = {
//        order: 'name',
//        limit: 3,
//        page: 2
//    };
//
//    $scope.loadStuff = function () {
//        $scope.promise = $timeout(function () {
//            // loading
//        }, 2000);
//    };
//
//    $scope.logItem = function (item) {
//        console.log(item.name, 'was selected');
//    };
//
//    $scope.logOrder = function (order) {
//        console.log('order: ', order);
//    };
//
//    $scope.logPagination = function (page, limit) {
//        console.log('page: ', page);
//        console.log('limit: ', limit);
//    }
//}]);



angular.module('userApp').controller('nutritionController', ['$mdEditDialog', '$q', '$timeout', '$scope', function ($mdEditDialog, $q, $timeout, $scope) {
  'use strict';

  $scope.options = {
    rowSelection: true,//
//    multiSelect: true,
    autoSelect: true,//
//    decapitate: false,
    largeEditDialog: false,//
    boundaryLinks: false,//
//    limitSelect: true,
    pageSelector: true//
  };


  $scope.selected = [];

  $scope.query = {
    order: 'name',
    limit: 5,
    page: 1
  };


  $scope.logPagination = function(page, limit) {
    console.log('Scope Page: ' + $scope.query.page + ' Scope Limit: ' + $scope.query.limit);
    console.log('Page: ' + page + ' Limit: ' + limit);

    $scope.promise = $timeout(function () {
    }, 2000);
  };

//  $scope.deselect = function (item) {
//    console.log(item.name, 'was deselected');
//  };
//
//  $scope.log = function (item) {
//    console.log(item.name, 'was selected');
//  };

  $scope.loadStuff = function () {
    $scope.promise = $timeout(function () {
    }, 2000);
  };

  $scope.onReorder = function(order) {

    console.log('Scope Order: ' + $scope.query.order);
    console.log('Order: ' + order);

    $scope.promise = $timeout(function () {

    }, 2000);
  };

}]);