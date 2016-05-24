'use strict';

angular.module('mainApp')
    .controller('MasterCtrl', function ($scope, $location, djangoAuth, $rootScope, $mdToast) {
        $scope.openMenu = function($mdOpenMenu, ev) {
            var originatorEv = ev;
            $mdOpenMenu(ev);
        };

        $scope.statusSaveToast = function(text) {
            $mdToast.show(
                $mdToast.simple()
                    .textContent(text)
                    .position("top right")
                    .hideDelay(3000)
            );
        };

        $scope.leftSidebarList = [
            {"title": "Personal Info", "link": "personal"},
            {"title": "Projects", "link": "projects"},
            {"title": "Tasks", "link": "tasks"},
            //{"title": "Progress", "link": "progress"},
            //{"title": "Teams", "link": "teams"},
            //{"title": "Activity", "link": "activity"},
        ];

        $scope.getTaskProject = function(activity) {
            if (activity.task) {
                return '#/user/tasks/' + activity.task.id ;
            };

            if (activity.project) {
                return '#/user/projects/' + activity.project.id ;
            };
        };
        $rootScope.searchPhrase = '';

        $scope.globalSearch = function(searchText) {
            $rootScope.searchPhrase = searchText;
            $location.url('/user/search/');
        };

        var handleSuccess = function (data) {
            $scope.response = data;
            $location.url('/');
        };

        var handleError = function (data) {
            $scope.response = data;
        };


        $scope.logout = function () {
            djangoAuth.logout()
                .then(handleSuccess, handleError);
        };

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
            $location.path('/').replace();
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

        $scope.$on('social_links', function (ev, data){
            $scope.social_links = data;
        });
    });
