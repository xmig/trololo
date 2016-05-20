angular.module('userApp').controller('taskCreateCtrl', ['$scope', 'projectService', '$rootScope', '$http', '$window', '$mdDialog', '$mdMedia', '$location', '$routeParams', 'taskService', 'taskSelectedService', '$timeout', '$mdSidenav', '$log',
    function($scope, projectService, $rootScope, $http, $window, $mdDialog, $mdMedia, $location, $routeParams, taskService, taskSelectedService, $timeout, $mdSidenav, $log)
{
    $scope.task_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/task_create.html';

// for dropdown <choose projects>
    $scope.projects = {}
    projectService.get(function(data) {
        $scope.projects = data.results;
        console.log("---------------", $scope.projects)
    })


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

    // set project_id
    $scope.taskData.project = $routeParams.project_id;

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
        // TASK CALCULATE
        $scope.taskData = taskSelectedService.get({ id: $scope.task_id }, function (response) {
            response.deadline_date = new Date(response.deadline_date);
//            response.project = response.project_obj.id
            $scope.taskData = response;
                        console.log('[[[$scope.taskData]]]', $scope.taskData)
                                            console.log('----$scope.taskData.members---', $scope.taskData.members, $scope.taskData.members_info)

            $scope.taskDataCopy = JSON.parse(JSON.stringify(response));
                        console.log('[[[$scope.taskDataCopy]]]', $scope.taskDataCopy)

//            $scope.taskData.project
//            console.log('EDIT', response.project)
        });
    }


    $scope.taskData = {members_info: []};

//    $scope.saveTask = function() {
//        $scope.taskData.tags = [];
//
//        if ($scope.task_id) {
//            // EDIT
//            $scope.taskData.id = $scope.task_id;
//            $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
//                return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
//            });
//
//            $scope.taskData.project = $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/projects/' + $scope.taskData.project + '/';
//
//            taskSelectedService.update($scope.taskData, function(response) {
//                response.deadline_date = new Date(response.deadline_date);
//                $scope.taskData = response;
//                if (typeof response.id !== 'undefined' && response.id > 0) {
//                    $window.location.href = '#/user/tasks/' + $scope.taskData.id;
//                }
//            });
//        } else {
//            $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
//                return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
//            });
//            taskService.create($scope.taskData, function(response) {
//                response.deadline_date = new Date(response.deadline_date);
//                $scope.taskData = response;
//                if (typeof response.id !== 'undefined' && response.id > 0) {
//                    $window.location.href = '#/user/tasks/' + response.id;
//                }
//
//            }, function(error){
////                console.log("++error++", error)
//            });
//
//        }
//    };


    $scope.saveTask = function(){
        $scope.saveTask.tags = [];

        if ($scope.task_id) {
            var mem = angular.equals($scope.taskDataCopy.members_info, $scope.taskData.members_info);
            //        console.log(angular.equals($scope.projectDataCopy.members_data, $scope.projectData.members_data));

            if ($scope.taskDataCopy.name !== $scope.taskData.name ||
                $scope.taskDataCopy.description !== $scope.taskData.description ||
                $scope.taskDataCopy.project !== $scope.taskData.project ||
                $scope.taskDataCopy.status !== $scope.taskData.status ||
                $scope.taskDataCopy.type !== $scope.taskData.type ||
                $scope.taskDataCopy.label !== $scope.taskData.label ||
                $scope.taskDataCopy.estimate_minutes !== $scope.taskData.estimate_minutes ||
                (new Date($scope.taskDataCopy.deadline_date) - $scope.taskData.deadline_date) !== 0 || mem !== true){
//                console.log("$scope.projectDataCopy.name", $scope.projectData.name, $scope.projectDataCopy.date_started)
                $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
                    return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
                });
                console.log('PROJECTS', $scope.taskDataCopy.project, $scope.taskData.project)


                taskSelectedService.update(
                    {id: $scope.task_id},
                    $scope.taskData,
                    function (response){
                        response.deadline_date = new Date(response.deadline_date);
                        $scope.taskDataCopy = response;
                        $window.location = '#/user/tasks/' + $scope.taskDataCopy.id;
                        $scope.statusSaveToast('Saved!');
                    },
                    function (response){
//                        console.log('response', response)

                        console.log('taskDataCopy.project', $scope.taskDataCopy.project_obj.id, $scope.taskData.project_obj.id)
                        var err_message = "Error status: " + response.statusText + " StatusText: " + response.statusText;
                        $log.debug(err_message);
                        $scope.statusSaveToast('Some error, contact admin.');
                    }
                )
            } else {
                $scope.statusSaveToast('Any change!');
            }
        } else {
            $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
                return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
            });
            taskService.create($scope.taskData, function(response) {
                response.deadline_date = new Date(response.deadline_date);
                $scope.taskData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/tasks/' + response.id + '/';
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