'use strict';

/**
 * @ngdoc function
 * @name mainApp.controller:RestrictedCtrl
 * @description
 * # RestrictedCtrl
 * Controller of the mainApp
 */
angular.module('mainApp')
  .controller('RestrictedCtrl', function ($scope, $location) {
    $scope.$on('djangoAuth.logged_in', function() {
      $location.path('/');
    });
  });
