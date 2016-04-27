angular.module('userApp').controller('taskCreateCtrl', ['$scope', '$rootScope', '$http', '$window', '$mdDialog', '$mdMedia', '$routeParams', 'taskService', 'task_selectedService',
    function($scope, $rootScope, $http, $window, $mdDialog, $mdMedia, $routeParams, taskService, task_selectedService)
{
    $scope.task_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/task_create.html';

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

//    var action = $routeParams.action;
//
//    // PROJECT CALCULATE
//    projectSelectedService.get({ id: $routeParams.id }, function (data) {
//        $scope.project = data;
//    });

    $scope.taskData = {};

    $scope.taskStatuses = [
        {'title': 'Breakthrough', 'id':'breakthrough'},
        {'title': 'In_progress', 'id':'in_progress'},
        {'title': 'Finished', 'id':'finished'},
        {'title': 'Undefined', 'id':'undefined'}
    ];

    $scope.visibleByList = [
        {'title': 'Members', 'id':'members'},
        {'title': 'Particular_user', 'id':'particular_user'},
        {'title': 'All_users', 'id':'all_users'},
        {'title': 'Undefined', 'id':'undefined'}

    ];

    $scope.taskLabels = [
        {'title':'Undefined', 'id':'undefined'},
        {'title': 'Red', 'id':'red'},
        {'title': 'Orange', 'id':'orange'},
        {'title': 'Green', 'id':'green'},
    ];

    $scope.taskTypes = [
        {'title': 'Undefined', 'id':'undefined'},
        {'title': 'Bug', 'id':'bug'},
        {'title': 'Feature', 'id':'feature'}
    ];





    if ($scope.task_id) {
        // EDIT
        // PROJECT CALCULATE
        task_selectedService.get({ id: $scope.task_id }, function (data) {
            $scope.taskData = data;
        });
    }

    $scope.saveTask = function() {
        $scope.taskData.tags = [];

        if ($scope.task_id) {
            // EDIT
            $scope.taskData.id = $scope.task_id;

            task_selectedService.update($scope.taskData, function(response) {
                $scope.taskData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/tasks/' + $scope.taskData.id;
                }
            });
        } else {
            taskService.create($scope.taskData, function(response) {
                $scope.taskData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/tasks/' + response.id + '/edit';
                }
            });
        }
    };

}])
.config(function($mdDateLocaleProvider) {
  $mdDateLocaleProvider.formatDate = function(date) {
    return date ? moment(date).format('DD-MM-YYYY') : '';
  };

  $mdDateLocaleProvider.parseDate = function(dateString) {
    var m = moment(dateString, 'DD-MM-YYYY', true);
    return m.isValid() ? m.toDate() : new Date(NaN);
  };
});