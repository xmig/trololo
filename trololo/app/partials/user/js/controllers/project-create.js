angular.module('userApp').controller('projectCreateCtrl', ['$scope', '$filter', '$rootScope', '$http', '$window', '$mdDialog', '$mdMedia', '$location', '$routeParams', 'projectService', 'projectSelectedService', '$timeout', '$mdSidenav', '$log',
    function($scope, $filter, $rootScope, $http, $window, $mdDialog, $mdMedia, $location, $routeParams, projectService, projectSelectedService, $timeout, $mdSidenav, $log)
{
    $scope.project_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/project_create.html';

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

    $scope.projectData = {};

    $scope.projectStatuses = [
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

    if ($scope.project_id) {
        // EDIT
        // PROJECT CALCULATE
        projectSelectedService.get({ id: $scope.project_id }, function (data) {
            data.date_started = new Date(data.date_started);
            data.date_finished = new Date(data.date_finished);
            $scope.projectData = data;
        });
    }

    $scope.saveProject = function() {
        $scope.projectData.tags = [];

        if ($scope.project_id) {
            // EDIT
            $scope.projectData.id = $scope.project_id;

            $scope.projectData.members = $scope.projectData.members_data.map(function (user, index) {
                return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
            });

            projectSelectedService.update($scope.projectData, function(response) {
                response.date_started = new Date(response.date_started);
                response.date_finished = new Date(response.date_finished);
                $scope.projectData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/' + $scope.projectData.id;
                }
            });
        } else {
            projectService.create($scope.projectData, function(response) {
                response.date_started = new Date(response.date_started);
                response.date_finished = new Date(response.date_finished);
                $scope.projectData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/' + response.id;
                }
            });
        }
    };
//    $scope.projectData.date_started = $filter('date')($scope.projectData.date_started, "dd/MM/yyyy");
//    $scope.projectData.date_finished = $filter('date')($scope.projectData.date_finished, "dd/MM/yyyy");
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