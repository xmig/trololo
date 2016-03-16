'use strict';

angular.module('mainApp')
    .controller('MasterCtrl', function ($scope, $location, djangoAuth) {
        // Assume user is not logged in until we hear otherwise
        $scope.authenticated = false;
        // Wait for the status of authentication, set scope var to true if it resolves
        djangoAuth.authenticationStatus(true).then(function () {
            $scope.authenticated = true;
        });
        // Wait and respond to the logout event.
        $scope.$on('djangoAuth.logged_out', function () {
            $scope.authenticated = false;
        });
        // Wait and respond to the log in event.
        $scope.$on('djangoAuth.logged_in', function () {
            $scope.authenticated = true;
        });
        // If the user attempts to access a restricted page, redirect them back to the main page.
        $scope.$on('$routeChangeError', function (ev, current, previous, rejection) {
            console.error("Unable to change routes.  Error: ", rejection);
            $location.path('/restricted').replace();
        });
        // Registration flag
        $scope.complete = false;
        $scope.$on('registrationComplete', function (ev, data) {
            console.log('data', data);
            $scope.complete = data;
        });
        //Reset password flag
        $scope.resetPasswordFlag = false;
        $scope.$on('resetPasswordEv', function (ev, data) {
            $scope.resetPasswordFlag = data;
        });
    });
