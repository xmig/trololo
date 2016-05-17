angular.module('userApp').controller('tasksCtrl', ['$scope', '$rootScope', '$http', 'taskService', 'activityListService', '$mdDialog', '$mdMedia', '$routeParams', 'projectService',
    function($scope, $rootScope, $http, taskService, activityListService, $mdDialog, $mdMedia, $routeParams, projectService){

    $scope.tasks = {data: []};
// for dropdown in popup <choose projects>
    $scope.projects = projectService.get(function(data) {
//        $scope.projects.data = data.results;
//        console.log("---------------", data.results)
    })


/* for datepicker */
     $scope.myDate = new Date();

     $scope.minDate = new Date(
         $scope.myDate.getFullYear(),
         $scope.myDate.getMonth() - 2,
         $scope.myDate.getDate());

     $scope.maxDate = new Date(
         $scope.myDate.getFullYear(),
         $scope.myDate.getMonth() + 2,
         $scope.myDate.getDate());

     $scope.onlyWeekendsPredicate = function(date) {
        var day = date.getDay();
        return day === 0 || day === 6;
     }


/* for popup */
    $scope.popRegistr = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            $mdDialog.show({
                    scope: $scope,        // use parent scope in template
                    preserveScope: true,  // use parent scope
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



//    $scope.getStatuses = function () {
//        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
//    };
//
//    $scope.getTypes = function () {
//        return ['bug', 'feature', 'undefined'];
//    };
/* end - for popup */




    /* ACTIVITY INFO */  //- sorting, view, pagination
    $scope.activitySortType = 'created_at'; // set the default sort type
    $scope.activitySortDirection = true;  // set the default sort order
    $scope.activityPageSize = 10;
    $scope.activityPage = 1;

    $scope.viewActivityVariants = ["5", "10", "20", "50", "All"];

    $scope.activitySortVariants = [
        {title: "by Date Asc", type: 'created_at', direction: true},
        {title: "by Date Desc", type: 'created_at', direction: false},
        {title: "by Message Asc", type: 'message', direction: true},
        {title: "by Message Desc", type: 'message', direction: false}
    ];

    var reloadActivity = function() {
        var sorting = ($scope.activitySortDirection ? '' : '-') + $scope.activitySortType;
        var params = {
            'page': $scope.activityPage,
            'page_size': $scope.activityPageSize,
            'ordering': sorting
        }

        activityListService.get(params, function (data) {
            $scope.activities = {}
            $scope.activities.data = data.results;
            $scope.activities.count = $scope.activities.data.length;
//            console.log($scope.activities.data);
        });
    };

    $scope.activitySort = function(sortInfo) {
        $scope.activitySortType = sortInfo.type;
        $scope.activitySortDirection = sortInfo.direction;
        $scope.activityPage = 1;
        reloadActivity();
    };

    $scope.viewActivity = function(viewInfo) {
        if (viewInfo === 'All') {
            $scope.activityPageSize = undefined;
        } else {
            $scope.activityPageSize = viewInfo;
        }
        $scope.activityPage = 1;
        reloadActivity();
    };

    reloadActivity();


/* NOTIFICATION INFO */
    $scope.notificationSortType = 'created_at'; // set the default sort type
    $scope.notificationSortDirection = true;  // set the default sort order
    $scope.notificationPageSize = 10;
    $scope.notificationPage = 1;

    $scope.viewNotificationVariants = ["5", "10", "20", "50", "All"];

    $scope.notificationSortVariants = [
        {title: "by Date Asc", type: 'created_at', direction: true},
        {title: "by Date Desc", type: 'created_at', direction: false},
        {title: "by Message Asc", type: 'message', direction: true},
        {title: "by Message Desc", type: 'message', direction: false}
    ];

    var reloadNotification = function() {
        var sorting = ($scope.notificationSortDirection ? '' : '-') + $scope.notificationSortType;
        var params = {
            'page': $scope.notificationPage,
            'page_size': $scope.notificationPageSize,
            'ordering': sorting,
            'for_cu':1
        }

        activityListService.get(params, function (data) {
            $scope.notifications = {}
            $scope.notifications.data = data.results;
            $scope.notifications.count = $scope.notifications.data.length;
        });
    };

    $scope.notificationSort = function(sortInfo) {
        $scope.notificationSortType = sortInfo.type;
        $scope.notificationSortDirection = sortInfo.direction;
        $scope.notificationPage = 1;
        reloadNotification();
    };

    $scope.viewNotification = function(viewInfo) {
        if (viewInfo === 'All') {
            $scope.notificationPageSize = undefined;
        } else {
            $scope.notificationPageSize = viewInfo;
        }

        $scope.notificationPage = 1;
        reloadNotification();
    };

    reloadNotification();


/* TASK INFO */
    $scope.taskSortType = 'title'; // set the default sort type
    $scope.taskSortDirection = true;  // set the default sort order
    $scope.taskPageSize = 500000000;
    $scope.taskPage = 1;

    $scope.viewTaskVariants = ["5", "10", "20", "50", "All"];

//    $scope.taskSortVariants = [
//        {title: "by Title Asc", type: 'name', direction: true},
//        {title: "by Title Desc", type: 'name', direction: false},
//        {title: "by Status Asc", type: 'status', direction: true},
//        {title: "by Status Desc", type: 'status', direction: false}
//    ];

    $scope.myTasksSortVariants = [
        {value: 'created_at',
         option: 'by Date'},
        {value: 'created_by',
         option: 'by Author'},
//        {value: '',
//         option: 'by Project'},
        {value: 'type',
         option: 'by Type'},
        {value: 'label',
         option: 'by Lable'},
        {value: 'status',
         option: 'by Status'}
      ];

    $scope.allTasksSortVariants = [
        {value: 'members',
         option: 'by Member'},
        {value: 'created_at',
         option: 'by Date'},
        {value: 'created_by',
         option: 'by Author'},
//        {value: '',
//         option: 'by Project'},
        {value: 'type',
         option: 'by Type'},
        {value: 'label',
         option: 'by Lable'},
        {value: 'status',
         option: 'by Status'}
      ];

    $scope.showMyTasks = {
        checked: false
    };

    $scope.showMyProjectTasks = {
        project: null
    };

    $scope.showMyUserTasks = {
        user: null
    };

    $scope.tag = $routeParams.task_tag;

    var reloadTask = function() {
        var sorting = ($scope.taskSortDirection ? '' : '-') + $scope.taskSortType;
        var params = {
            'page': $scope.taskPage,
            'page_size': $scope.taskPageSize,
            'ordering': sorting,
            'for_cu':1
        }

        if ($scope.tag !== undefined) {
            params.tag = $scope.tag;
        };

        taskService.get(params, function (data) {
            $scope.tasks = {}
            $scope.tasks.data = data.results;
            $scope.tasks.count = $scope.tasks.data.length;

            $scope.my_tasks = {};
            var tasks_list = [];
            $scope.members_ids = [];
            $scope.members = [];


            for (var i=0; i<data.results.length; i++) {
                var task_i = data.results[i];

                if (task_i.members.indexOf($scope.userPersonalData.id) != -1) {
                    tasks_list.push(task_i);
                }
                for (var index=0; index<task_i.members_info.length; index++){
                    current_member = task_i.members_info[index];
                    if ($scope.members_ids.indexOf(current_member.id) == -1) {
                        $scope.members.push(current_member);
                        $scope.members_ids.push(current_member.id);
                    }
                }
            }

            $scope.my_tasks.data = tasks_list;
            $scope.my_tasks.count = tasks_list.length;
        });
    };

    $scope.taskSort = function(sortInfo) {
        $scope.taskSortType = sortInfo.type;
        $scope.taskSortDirection = sortInfo.direction;
        $scope.taskPage = 1;
        reloadTask();
    };

    $scope.viewTask = function(viewInfo) {
        if (viewInfo === 'All') {
            $scope.taskPageSize = undefined;
        } else {
            $scope.taskPageSize = viewInfo;
        }

        $scope.taskPage = 1;
        reloadTask();
    };

    reloadTask();


//    $scope.reloadTasks();


//    taskService.get(params, function (data) {
//            $scope.tasks = {}
//            $scope.tasks.data = data.results;
//            $scope.tasks.count = $scope.tasks.data.length;
//
//            $scope.my_tasks_ovner = {};
//            var tasks_list_owner = [];
//
//            if (tasks_list_owner.members.indexOf($scope.userPersonalData.id) == -1) {
//                tasks_list.push(task_i);
//            }
//          }
//
//            $scope.my_tasks_ovner.data = tasks_list;
//            $scope.my_tasks.count = tasks_list.length;
//        });


    $scope.all_members = [{'id': undefined, 'username': 'All'}];
    $scope.all_project = [{project_obj: {'id': undefined, 'name': 'All'}}];


    $scope.onlyMyTasks = function(value, index, array) {

        var members_id_list = [];
        for (var i=0; i<value.members_info.length; i++) {
            members_id = value.members_info[i];
            members_id_list.push(members_id.id)
        }
        if (!$scope.showMyTasks.checked) {
            return true;
        } else if (members_id_list.indexOf($scope.userPersonalData.id) != -1) {
            return true;
        }
        return false;
    };

//    $scope.onlyMyProjectTasks = function(value, index, array) {
//        if (!$scope.showMyProjectTasks.project) {
//            return true;
//        } else if ($scope.showMyProjectTasks.project == value.project_obj.id) {
//
//            return true;
//        } else {
//            return false;
//        }
//    };


    $scope.onlyMyProjectTasks = function(value, index, array) {
        if (value === undefined) {
        }
        for ( var j=0; j<index; j++) {
            if (value.project_obj.id === array[j].project_obj.id) {
                return false;
            }
        }

        return true
    };

    $scope.selectedProjectTasks = function(value, index, array) {
        if (!$scope.showMyProjectTasks.project) {
            return true;
        } else if ($scope.showMyProjectTasks.project == value.project_obj.id) {

            return true;
        } else {
            return false;
        }
    };

    $scope.onlyMyUserTasks = function(value, index, array) {
        if (value === undefined) {
        }
        for ( var j=0; j<index; j++) {
            if (value.owner.id === array[j].owner.id) {
                return false;
            }
        }

        return true
    };

    $scope.selectedUserTasks = function(value, index, array) {
        if (!$scope.showMyUserTasks.user) {
            return true;
        } else {
            for (var i=0; i<value.members_info.length; i++){
                if ($scope.showMyUserTasks.user == value.members_info[i].id){
                    return true;
                }
            }

            return false;
        }
    }


// HARDCODE !!!
    $scope.labels = [
        {value: 'undefined',
         option: 'Undefined'},
        {value: 'red',
         option: 'Red'},
        {value: 'orange',
         option: 'Orange'},
        {value: 'green',
         option: 'Green'},
    ];

    $scope.types = [
        {value: 'undefined',
         option: 'Undefined'},
        {value: 'bug',
         option: 'Bug'},
        {value: 'feature',
         option: 'Feature'}
    ];

    $scope.statuses = [
        {value: 'undefined',
         option: 'Undefined'},
        {value: 'breakthrough',
         option: 'Breakthrough'},
        {value: 'in progress',
         option: 'In progress'},
        {value: 'finished',
         option: 'Finished'}
    ];
    
// END HARDCODE !!!    



/* for popup */
    $scope.popRegistr = function (ev) {
            var useFullScreen = ($mdMedia('sm') || $mdMedia('xs')) && $scope.customFullscreen;
            $mdDialog.show({
                    scope: $scope,        // use parent scope in template
                    preserveScope: true,  // use parent scope
                    controller: DialogController,
//                    templateUrl: 'register.tmpl.html',
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


//    $scope.getStatuses = function () {
//        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
//    };
//
//    $scope.getTypes = function () {
//        return ['bug', 'feature', 'undefined'];
//    };

/* end - for popup */


//CHECKBOXES//

//for checkbox members//
    $scope.items = [1,2,3,4,5];
      $scope.selected = [];

      $scope.toggle = function (item, list) {
        var idx = list.indexOf(item);
        if (idx > -1) {
          list.splice(idx, 1);
        }
        else {
          list.push(item);
        }
      };

      $scope.exists = function (item, list) {
        return list.indexOf(item) > -1;
      };

/* for standard checkboxes */
//     $scope.items = [1,2,3,4,5];
//          $scope.selected = [1];
//          $scope.toggle = function (item, list) {
//            var idx = list.indexOf(item);
//            if (idx > -1) {
//              list.splice(idx, 1);
//            }
//            else {
//              list.push(item);
//            }
//          };
//
//          $scope.exists = function (item, list) {
//            return list.indexOf(item) > -1;
//          };
//
//          $scope.isIndeterminate = function() {
//            return ($scope.selected.length !== 0 &&
//                $scope.selected.length !== $scope.items.length);
//          };
//
//          $scope.isChecked = function() {
//            return $scope.selected.length === $scope.items.length;
//          };
//
//          $scope.toggleAll = function() {
//            if ($scope.selected.length === $scope.items.length) {
//              $scope.selected = [];
//            } else if ($scope.selected.length === 0 || $scope.selected.length > 0) {
//              $scope.selected = $scope.items.slice(0);
//            }




    $scope.editComment = function (event, dessert) {
        event.stopPropagation(); // in case autoselect is enabled

        var editDialog = {
            modelValue: dessert.comment,
            placeholder: 'Add a comment',
            save: function (input) {
                if(input.$modelValue === 'Donald Trump') {
                    return $q.reject();
                }
                if(input.$modelValue === 'Bernie Sanders') {
                    return dessert.comment = 'FEEL THE BERN!'
                }
                dessert.comment = input.$modelValue;
            },
            targetEvent: event,
            title: 'Add a comment',
            validators: {
                'md-maxlength': 30
            }
        };

        var promise;

        if($scope.options.largeEditDialog) {
            promise = $mdEditDialog.large(editDialog);
        } else {
            promise = $mdEditDialog.small(editDialog);
        }

        promise.then(function (ctrl) {
            var input = ctrl.getInput();

            input.$viewChangeListeners.push(function () {
                input.$setValidity('task_test', input.$modelValue !== 'task_test');
            });
        });
    };

    $scope.getTypes = function () {
        return ['Candy', 'Ice cream', 'Other', 'Pastry'];
    };
    /* Test table data end */

}]);


/* for popup */
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
/* end - for popup */
