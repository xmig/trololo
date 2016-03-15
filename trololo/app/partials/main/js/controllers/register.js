'use strict';

angular.module('mainApp')
    .controller('RegisterCtrl', function ($scope, $rootScope, djangoAuth, Validate) {
        $scope.model = {'username': '', 'password': '', 'email': ''};
        $scope.errors = [];
        $scope.register = function (formData) {

            Validate.form_validation(formData, $scope.errors);
            if (!formData.$invalid) {
                djangoAuth.register($scope.model.username, $scope.model.password1, $scope.model.password2, $scope.model.email)
                    .then(function (data) {
                        // success case
                        $rootScope.$broadcast('registrationComplete', true);
                        $scope.cancel();
                    }, function (data) {
                        // error case
                        $scope.errors = data;
                    });
            }
        };
        $scope.resetErrors = function (value) {
            if ($scope.errors && $scope.errors[value] && $scope.errors[value].length >= 1) {
                console.log('clear');
                $scope.errors[value] = [];
            }
        }
    });
