angular.module('userApp').controller('taskCreateCtrl', ['projectStatusService', '$scope', 'projectService', '$rootScope', '$http', '$window', '$mdDialog', '$mdMedia', '$location', '$routeParams', 'taskService', 'taskSelectedService', '$timeout', '$mdSidenav', '$log',
                                               function(projectStatusService, $scope, projectService, $rootScope, $http, $window, $mdDialog, $mdMedia, $location, $routeParams, taskService, taskSelectedService, $timeout, $mdSidenav, $log)
{
    $scope.task_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/task_create.html';

// for dropdown <choose projects>
    $scope.projects = {}
    projectService.get(function(data) {
        $scope.projects = data.results;
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

    $scope.gettaskProjectStatuses = function(response){
        $scope.taskProjectStatuses = projectStatusService.get_all({'project': response.project}, function (resp) {
            $scope.taskProjectStatuses = resp;    // resp - array of project statuses
            $scope.taskData = response;
         })
    }

    if ($scope.task_id) {
        // EDIT
        // TASK CALCULATE
        taskSelectedService.get({ id: $scope.task_id }, function (response) {
            //$scope.taskData = response;
            response.deadline_date = new Date(response.deadline_date);
            $scope.gettaskProjectStatuses(response)


            $scope.taskDataCopy = JSON.parse(JSON.stringify(response));
                        console.log('[[[$scope.taskDataCopy]]]', $scope.taskDataCopy)

//            $scope.taskData.project
        });
    }


    $scope.taskData = {members_info: []};


//TRY
    var selectedProject = $location.search();
    if (Object.keys(selectedProject).length) {
        $scope.taskData.project = +selectedProject['project_id']
    }
///

    $scope.saveTask = function(){
        $scope.saveTask.tags = [];

        if ($scope.task_id) {

            var mem = angular.equals($scope.taskDataCopy.members_info, $scope.taskData.members_info);

            if ($scope.taskDataCopy.name !== $scope.taskData.name ||
                $scope.taskDataCopy.description !== $scope.taskData.description ||
                $scope.taskDataCopy.assigned_member !== $scope.taskData.assigned_member ||
                $scope.taskDataCopy.project !== $scope.taskData.project ||
                !angular.equals($scope.taskDataCopy.status, $scope.taskData.status) ||   // compare objects
                $scope.taskDataCopy.type !== $scope.taskData.type ||
                $scope.taskDataCopy.label !== $scope.taskData.label ||
                $scope.taskDataCopy.estimate_minutes !== $scope.taskData.estimate_minutes ||
                (new Date($scope.taskDataCopy.deadline_date) - $scope.taskData.deadline_date) !== 0 || mem !== true){
                $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
                    return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
                });


                taskSelectedService.update({'id': $scope.task_id}, $scope.taskData, function (response){
                        response.deadline_date = new Date(response.deadline_date);
                        $scope.taskDataCopy = response;
                        $window.location = '#/user/tasks/' + $scope.taskDataCopy.id;
                        $scope.statusSaveToast('Saved!');
                    },

                    function (response){
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

    $scope.changeProject = function(id){
        $scope.taskProjectStatuses = projectStatusService.get_all({'project': id}, function (resp) {
            $scope.taskProjectStatuses = resp;
                console.log('$scope.taskProjectStatuses!!!', $scope.taskProjectStatuses)
            if(resp[0].id){
                try {
                        $scope.taskData.status.id = resp[0].id
                    }
                catch(err) {
                    }
            }
         })
    }


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