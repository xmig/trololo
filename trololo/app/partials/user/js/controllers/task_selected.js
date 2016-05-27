angular.module('userApp').controller('taskSelectedCtrl', ['taskCommentService', 'personalInfoService', 'taskFilesSelectedService', '$cookies', 'taskSelectedFileUploadService', '$scope', '$rootScope', '$http', 'taskSelectedService', 'activityListService', '$mdDialog', '$mdMedia', '$routeParams', '$timeout', '$mdSidenav', 'task_tagService', '$log', 'personalInfoService', '$window', '$location','taskCommentSelectedService',
                                                 function(taskCommentService, personalInfoService, taskFilesSelectedService, $cookies, taskSelectedFileUploadService, $scope, $rootScope, $http, taskSelectedService, activityListService, $mdDialog, $mdMedia, $routeParams, $timeout, $mdSidenav, task_tagService, $log, personalInfoService, $window, $location, taskCommentSelectedService){


    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.partialPath = '/static/user/templates/task_selected.html';

    //$scope.location = $routeParams.userLocation;
    //console.log("---", $routeParams.taskid);


// TAGS - patch for tags
    $scope.task = {tags: []};


//    $scope.task = taskSelectedService.get({"id": $routeParams.taskid}, function() {
//         console.log($scope.task);
//    })


    taskSelectedService.get({"id": $routeParams.taskid}, function(response) {
         $scope.task = response;
         console.log("DDDDD", $scope.task);
         console.log("DDDDD", $scope.task.files);
         
    }, function(error){
//        console.log("ERROR"); // if task doesn't exist - go to main page
        $window.location.href = "#/"
    })



// TAG manipulations
    // TAG manipulations
    $scope.searchTag = function(tag) {
        $location.url('/user/tasks/tag/' + tag.name);
    };

    $scope.addTag = function(tag) {
        task_tagService.add_tag(
            {'id': $routeParams.taskid, 'tag_name': tag.name}, {}, function(response) {
            }, function () {
                $scope.task.tags.splice($scope.task.tags.length - 1, 1);
            }
        );
    };

    $scope.removeTag = function(tag) {
        tag_name = tag.name;

        task_tagService.delete_tag(
            {'id': $routeParams.taskid, 'tag_name': tag_name}, {}, function(response) {
            }, function () {
                $scope.task.tags.push(tag);
            }
        );
    };

    $scope.newTag = function(tag) {
        return {'name': tag};
    };
//



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

        activityListService.get(params, function (data) { //{"created_by": $routeParams.taskid.created_by},
            $scope.activities = {}
            $scope.activities.data = data.results;
            $scope.activities.count = $scope.activities.data.length;
            console.log("$scope.activities.data", $scope.activities.data);
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


/* COMMENT */
    $scope.commentSortType = 'created_at'; // set the default sort type
    $scope.commentSortDirection = true;  // set the default sort order
    $scope.commentPageSize = 10;
    $scope.commentPage = 1;

    $scope.viewCommentVariants = ['1',"5", "10", "20", "50", "All"];

    $scope.commentSortVariants = [
          {value: "created_at",
           option: "by Date Asc",
           direction: true
          },

          {value: "created_by__username",
           option: "by User Asc",
           direction: true
          }
//          {value: "comment",
//           option: "by Type"
//          },
    ];

    var reloadComment = function() {
        var sorting = ($scope.commentSortDirection ? '' : '-') + $scope.commentSortType;
        var params = {
            'page': $scope.commentPage,
            'page_size': $scope.commentPageSize,
            'ordering': sorting,
            'for_cu':1,
            'task': $routeParams.taskid
        }
        taskCommentService.get(params, function (data) {
            $scope.task.comments = data.results;
            $scope.task.comments.count = $scope.task.comments.length;
            console.log('data.results', data.results,'-----', $scope.task.comments.count);
        });
    };

    $scope.commentSort = function(sortInfo) {
    console.log("sortInfo", sortInfo)
        $scope.commentSortType = sortInfo.value;
        $scope.commentSortDirection = sortInfo.direction;
        $scope.commentPage = 1;
        console.log("11111", $scope.commentSortType)
        reloadComment();
    };


    $scope.viewComment = function(viewInfo) {
        if (viewInfo === 'All') {
            $scope.commentPageSize = 1000000;
        } else {
            $scope.commentPageSize = viewInfo;
        }

        $scope.commentPage = 1;
        reloadComment();
    };

    $scope.deleteTaskCommentPopup = function(ev, id, name) {
    ev.preventDefault();
        var confirm = $mdDialog.confirm()
              .title('Would you like to delete comment?')
              .textContent('Are you sure you mant to delete comment ' + name + "?")
              .ariaLabel('Lucky day')
              .targetEvent(ev)
              .ok('Delete')
              .cancel('Cancel');

        $mdDialog.show(confirm).then(
            function() {
                taskCommentSelectedService.remove_comment_task(
                    {id: id}, {},
                    function(resp) {

                        reloadComment();
                    }
                )
            }
        );
      };

    $scope.showAddCommentDialog = function(event) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'add_comment.tmpl.html',
            parent: angular.element(document.body),
            targetEvent: event,
            scope: $scope,
            preserveScope: true,
            clickOutsideToClose: true,
            fullscreen: false
        });
    };


 personalInfoService.get(function (data) {
        $scope.userAdditionData = {
            first_name: data.first_name,
            last_name: data.last_name,
            department: data.department,
            specialization: data.specialization,
            detailed_info: data.detailed_info,
            use_gravatar: data.use_gravatar,
            social_accounts: data.social_accounts
        };
        $scope.userPersonalData = data;
    });

    $scope.changeUserLocation = function(e, id){
    console.log("-----")
    e.preventDefault();
        if($scope.userPersonalData.id !== id){
            $window.location.href = '#/user/profile/' + id;
        } else {
            $window.location.href = '#/user/personal/';
        }
    };

    $scope.savetaskComment = function() {
        $scope.taskCommentData = {};
        $scope.taskCommentData.tags = [];
        $scope.taskCommentData.task = 'http://' + $window.location.host + '/tasks/' + $routeParams.taskid + '/';
        console.log('+++ $routeParams.id  +++', $window.location.host, $routeParams.taskid, $routeParams.taskid)
        $scope.taskCommentData.comment = $scope.comment_text;
        taskCommentService.create($scope.taskCommentData, function(response) {
            $scope.taskCommentData = response;
            if (typeof response.id !== 'undefined' && response.id > 0) {
                $window.location.href = '#/user/tasks/' + $routeParams.taskid + '/';
                $scope.statusSaveToast('Saved!');
            }
        });
    };
    reloadComment();


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
            'for_cu':1,
            'task_activities': $routeParams.id
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


    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
        //{"title": "Activity", "link": "activity"},
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


/* end - for popup */



    $scope.viewVariants = [
          "5",
          "10",
          "20",
          "50",
          "All"
      ];


//// TASK CALCULATE
//    taskSelectedService.get({ id: $routeParams.id }, function (data) {
//        $scope.task = data;
//    });



//** ADD/DELETE USERS in TASK MEMBERS TAB **//

//get authorized user
    $scope.user = personalInfoService.update($scope.userAdditionData, function(response) {
            $scope.userData = response;
            });

// TASK CALCULATE
    $scope.taskData = taskSelectedService.get({"id": $routeParams.taskid}, function (response) {
        $scope.taskData = response;
        $scope.taskData.assigned_member = response.assigned_member;                                              ////  *******


                        console.log('----$scope.taskData----', $scope.taskData)
                        console.log('----response----', response)

                        console.log('----$scope.taskData.members---', $scope.taskData.members, $scope.taskData.members_info)
                        console.log('----$scope.taskData.assigned_member---', $scope.taskData.assigned_member)


        $scope.taskCopy = JSON.parse(JSON.stringify(response));
                        console.log('----$scope.taskCopy----', $scope.taskCopy)
        });

// TASK SAVE

    $scope.taskData = {members_info: []};
    console.log('TESTING TASK', $scope.taskData)

    $scope.saveTask = function(){
        $scope.saveTask.tags = [];

//        taskSelectedService.get({"id": $routeParams.taskid}, function(response) {
//            $scope.taskData = response;
//                            console.log('[[[ response ]]]', response)
//            $scope.taskCopy = JSON.parse(JSON.stringify(response));
//                            console.log('[[[ taskData ]]]', $scope.taskData)
//                            console.log('[[[ taskCopy ]]]', $scope.taskCopy)

            if ($scope.taskCopy.members_info !== $scope.taskData.members_info) {
                            console.log('[[[ $scope.taskData.members_info ]]]', $scope.taskData.members_info)

                $scope.taskData.id = $routeParams.taskid;
                                console.log('[[[ $scope.taskData.id ]]]', $scope.taskData.id)

                $scope.taskData.members = $scope.taskData.members_info.map(function (user, index) {
                    return $location.protocol() + "://" + $location.host() + ":" + $location.port() + '/users/' + user.id + '/';
                });

                                            console.log('$scope.taskData.members', $scope.taskData.members)
                                            console.log('$scope.taskData.assigned_member', $scope.taskData.assigned_member)


                taskSelectedService.update({"id": $scope.taskData.id}, $scope.taskData, function(response) {
                    $scope.taskData = response;
                            console.log('$scope.taskData', $scope.taskData)
                    $window.location = '#/user/tasks/' + $scope.taskCopy.id;
                    $scope.statusSaveToast('Saved!');
                },

                    function (response){
                        console.log('response', response)
                        var err_message = "Error status: " + response.statusText + " StatusText: " + response.statusText;
                        $log.debug(err_message);
                        $scope.statusSaveToast('Some error, contact admin.');
                    }
                )
            } else {
                $scope.statusSaveToast('Any change!');
            };
        };



//File upload
    $scope.$on(
        'filesAdded', function(event, files) {
            $scope.files = files;
        }
    )

    $scope.onSubmit = function(){
        for (var i=0; i<$scope.files.length; i++) {
            var file = $scope.files[i];

            var formData = new FormData()
            formData.append('file_upload', file.lfFile);
            formData.append('task', $routeParams.taskid);

            taskSelectedFileUploadService.save(
                {},
                formData,
                function(data) {
                    $scope.task.files.push(data);
                    $scope.statusSaveToast('File added!');
                },
                function(err) {
                    var err_message = "Error status: " + response.statusText + " StatusText: " + response.statusText;
                    $log.debug(err_message);
                    $scope.statusSaveToast('Some error, contact admin.');
                }
            );
        }
    };


    $scope.deleteFilePopup = function(ev, id, name, index) {
    ev.preventDefault();
        var confirm = $mdDialog.confirm()
              .title('Would you like to delete file?')
              .textContent('Are you sure you mant to delete file ' + name + "?")
              .ariaLabel('Lucky day')
              .targetEvent(ev)
              .ok('Delete')
              .cancel('Cancel');

        $mdDialog.show(confirm).then(
            function() {
                taskFilesSelectedService.delete_file(
                    {id: id},
                    function(resp) {
                        $scope.task.files.splice(index, 1);
                    }
                )
            }
        );
    };

    $scope.getFileName = function(file_address) {
        return file_address.substring(file_address.lastIndexOf('/') + 1);
    }
}]);
