angular.module('userApp').controller('commentSelectedCtrl', ['$scope', '$rootScope', '$http', '$mdDialog', '$mdMedia', '$routeParams', '$mdSidenav', 'commentSelectedService', 'activityListService', 'taskService','personalInfoService', '$window',
    function($scope, $rootScope, $http, $mdDialog, $mdMedia, $routeParams, $mdSidenav, commentSelectedService, activityListService, taskService, personalInfoService, $window)
{
    $scope.partialPath = '/static/user/templates/project_selected.html';

    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"}
    ];
    $scope.isSectionSelected = function(section){
        return section === $scope.location;
    };
    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
        var timer;

        return function debounced() {
            var context = $scope,
                args = Array.prototype.slice.call(arguments);
            $timeout.cancel(timer);
            timer = $timeout(function() {
                timer = undefined;
                func.apply(context, args);
            }, wait || 10);
        };
    }

    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildDelayedToggler(navID) {
        return debounce(function() {
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        }, 200);
    }

    function buildToggler(navID) {
        return function() {
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        }
    }



    // PROJECT CALCULATE
    projectSelectedService.get({ id: $routeParams.id }, function (data) {
        $scope.project = data;
    });
}]);





angular.module('userApp').controller('taskCommentSelectedCtrl', ['$scope', '$rootScope', '$http', '$mdDialog', '$mdMedia', '$routeParams', 'taskSelectedService', 'taskCommentSelectedService', 'activityListService', 'taskService','personalInfoService', '$window',
    function($scope, $rootScope, $http, $mdDialog, $mdMedia, $routeParams, taskSelectedService, taskCommentSelectedService, activityListService, taskService, personalInfoService, $window)
{
    $scope.partialPath = '/static/user/templates/task_selected.html';

    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"}
    ];
    $scope.isSectionSelected = function(section){
        return section === $scope.location;
    };
    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
        var timer;

        return function debounced() {
            var context = $scope,
                args = Array.prototype.slice.call(arguments);
            $timeout.cancel(timer);
            timer = $timeout(function() {
                timer = undefined;
                func.apply(context, args);
            }, wait || 10);
        };
    }

    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildDelayedToggler(navID) {
        return debounce(function() {
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        }, 200);
    }

    function buildToggler(navID) {
        return function() {
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        }
    }



    // PROJECT CALCULATE
    taskSelectedService.get({ id: $routeParams.id }, function (data) {
        $scope.task = data;
    });
}]);