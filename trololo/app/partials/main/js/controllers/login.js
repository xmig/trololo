'use strict';

angular.module('mainApp')
    .controller('LoginCtrl', function ($scope, $rootScope, $location, djangoAuth, Validate) {
        console.log($scope.social_links);
        $scope.social_login = {
            'google': '/static/img/google_logo_35x35.png',
            'facebook': '/static/img/facebook-logo_35x35.png',
            'github': '/static/img/github_logo-35x35.png',
            'linkedin': '/static/img/linkedIn_logo_35x35.png'
        };
        $scope.model = {'username': '', 'password': ''};
        //$scope.complete = false;
        $scope.login = function (formData) {
            $scope.errors = [];
            Validate.form_validation(formData, $scope.errors);
            if (!formData.$invalid) {
                djangoAuth.login($scope.model.username, $scope.model.password)
                    .then(function (data) {
                        // success case
                        $scope.cancel();
                        $location.path("/");
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
        $scope.openResetPasswordModal = function () {
            $rootScope.$broadcast('resetPasswordEv', true);
            $scope.cancel();
        }
    });
