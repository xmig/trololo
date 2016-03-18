'use strict';

angular.module('mainApp')
    .controller('MainCtrl', function ($scope, $rootScope, $cookies, $location, djangoAuth, $mdDialog, $mdMedia) {
        $scope.popLogin = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: 'login.tmpl.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: useFullScreen
                })
                .then(function (answer) {
                    $scope.status = 'You said the information was "' + answer + '".';
                }, function () {
                    $scope.status = 'You cancelled the dialog.';
                    if($scope.resetPasswordFlag){
                        $scope.resetPasswordModal(ev);
                    }
                    $rootScope.$broadcast('resetPasswordEv', false);
                });

            $scope.$watch(function () {
                return $mdMedia('xs') || $mdMedia('sm');
            }, function (wantsFullScreen) {
                $scope.customFullscreen = (wantsFullScreen === true);
            });
        };

        $scope.popRegistr = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: 'register.tmpl.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: useFullScreen
                })
                .then(function (answer) {
                    $scope.status = 'You said the information was "' + answer + '".';
                }, function () {
                    $scope.status = 'You cancelled the dialog.';
                    if($scope.complete){
                        $scope.registerComplete(ev);
                    }
                    $rootScope.$broadcast('registrationComplete', false);
                });

            $scope.$watch(function () {
                return $mdMedia('xs') || $mdMedia('sm');
            }, function (wantsFullScreen) {
                $scope.customFullscreen = (wantsFullScreen === true);
            });
        };

        $scope.registerComplete = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            console.log('Register Complete');
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: 'registerComplete.tmpl.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: useFullScreen
                })
                .then(function (answer) {
                    $scope.status = 'You said the information was "' + answer + '".';

                }, function () {
                    $scope.status = 'You cancelled the dialog.';
                });

            $scope.$watch(function () {
                return $mdMedia('xs') || $mdMedia('sm');
            }, function (wantsFullScreen) {
                $scope.customFullscreen = (wantsFullScreen === true);
            });
        };

         $scope.resetPasswordModal = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: 'reset_pass.tmpl.html',
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: useFullScreen
                })
                .then(function (answer) {
                    $scope.status = 'You said the information was "' + answer + '".';
                }, function () {
                    $scope.status = 'You cancelled the dialog.';
                });

            $scope.$watch(function () {
                return $mdMedia('xs') || $mdMedia('sm');
            }, function (wantsFullScreen) {
                $scope.customFullscreen = (wantsFullScreen === true);
            });
        };


        $scope.login = function () {
            djangoAuth.login(prompt('Username'), prompt('password'))
                .then(function (data) {
                    handleSuccess(data);
                }, handleError);
        };

        $scope.logout = function () {
            djangoAuth.logout()
                .then(handleSuccess, handleError);
        };

        $scope.resetPassword = function () {
            djangoAuth.resetPassword(prompt('Email'))
                .then(handleSuccess, handleError);
        };

        $scope.register = function () {
            djangoAuth.register(prompt('Username'), prompt('Password'), prompt('Email'))
                .then(handleSuccess, handleError);
        };

        $scope.verify = function () {
            djangoAuth.verify(prompt("Please enter verification code"))
                .then(handleSuccess, handleError);
        };

        $scope.goVerify = function () {
            $location.path("/verifyEmail/" + prompt("Please enter verification code"));
        };

        $scope.changePassword = function () {
            djangoAuth.changePassword(prompt("Password"), prompt("Repeat Password"))
                .then(handleSuccess, handleError);
        };

        $scope.profile = function () {
            djangoAuth.profile()
                .then(handleSuccess, handleError);
        };

        $scope.updateProfile = function () {
            djangoAuth.updateProfile({
                    'first_name': prompt("First Name"),
                    'last_name': prompt("Last Name"),
                    'email': prompt("Email")
                })
                .then(handleSuccess, handleError);
        };

        $scope.confirmReset = function () {
            djangoAuth.confirmReset(prompt("Code 1"), prompt("Code 2"), prompt("Password"), prompt("Repeat Password"))
                .then(handleSuccess, handleError);
        };

        $scope.goConfirmReset = function () {
            $location.path("/passwordResetConfirm/" + prompt("Code 1") + "/" + prompt("Code 2"))
        };

        var handleSuccess = function (data) {
            $scope.response = data;
        };

        var handleError = function (data) {
            $scope.response = data;
        };

        $scope.show_login = true;
        $scope.$on("djangoAuth.logged_in", function (data) {
            $scope.show_login = false;
        });
        $scope.$on("djangoAuth.logged_out", function (data) {
            $scope.show_login = true;
        });
    });

function DialogController($scope, $mdDialog) {
  $scope.hide = function() {
    $mdDialog.hide();
  };

  $scope.cancel = function() {
    $mdDialog.cancel();
  };

  $scope.answer = function(answer) {
    $mdDialog.hide(answer);
  };
}
