'use strict';

angular.module('mainApp')
    .controller('PasswordresetCtrl', function ($scope, djangoAuth, Validate) {
        $scope.model = {'email': ''};
        $scope.complete = false;
        $scope.resetPassword = function (formData) {
            $scope.errors = [];
            Validate.form_validation(formData, $scope.errors);
            if (!formData.$invalid) {
                djangoAuth.resetPassword($scope.model.email)
                    .then(function (data) {
                        // success case
                        $scope.complete = true;
                        $scope.cancel();
                        console.log("Close reset modal");
                    }, function (data) {
                        // error case
                        $scope.errors = data;
                    });
            }
        };
        $scope.resetErrors = function (value) {
            if ($scope.errors && $scope.errors[value] && $scope.errors[value].length >= 1) {
                $scope.errors[value] = [];
            }
        }
    });
