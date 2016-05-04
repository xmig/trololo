angular.module('mainApp')
  .controller('addStatusCtrl', function ($scope, Validate, $mdDialog, $location, projectStatusService) {
    $scope.status_name = '';
  	$scope.complete = false;

  	$scope.getErrorText = function (resp) {
  	    var text = 'Error ' + resp.status + ': ' + resp.statusText + '<br /><br /> ';

  	    Object.keys(resp.data.detail).forEach(function (key, ind) {
  	        text += ('<b>' + key + '</b>: ' + resp.data.detail[key] + "<br />");
  	    })

  	    return text;
  	};

    $scope.addStatsus = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);

      if(!formData.$invalid) {
        projectStatusService.add_status(
            {
                'name': $scope.status_name,
                'project': 'http://' + $location.host() + '/projects/' + $scope.project.id + '/'
            }
        ).$promise
        .then(function(resp) {
            $scope.hide();

            $scope.reloadStatuses();
            var alert = $mdDialog.alert()
                .title('Complete')
                .textContent('Status was added!')
                .ok('Close');
            $mdDialog.show(alert)
                .finally(function() {
                    alert = undefined;
                });
            }, function(resp) {
                $scope.hide();

                console.log("Status: " + resp.status);
                if(resp.status !== 200) {
                    var err = $mdDialog.alert()
                        .title('Failure')
                        .htmlContent($scope.getErrorText(resp))
                        .ok('Close');
                    $mdDialog.show(err)
                        .finally(function() {
                            alert = undefined;
                        });
                }
            })
        }
    }
  });


angular.module('userApp').controller('projectSelectedCtrl', ['$scope', '$rootScope', '$http', '$mdDialog', '$mdMedia', '$routeParams', 'projectSelectedService', 'activityListService', 'taskService', 'project_tagService', '$timeout', '$mdSidenav', '$log', 'personalInfoService', '$window','commentSelectedService', 'commentService', 'projectStatusService', 'projectSelectedStatusService', '$location',
    function($scope, $rootScope, $http, $mdDialog, $mdMedia, $routeParams, projectSelectedService, activityListService, taskService, project_tagService, $timeout, $mdSidenav, $log, personalInfoService, $window,commentSelectedService, commentService, projectStatusService, projectSelectedStatusService, $location) {
    $scope.partialPath = '/static/user/templates/project_selected.html';

    // patch for tags
    $scope.project = {tags: []};

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

    // GET PROJECT STATUSES
    $scope.statusSortType = 'order_number'; // set the default sort type
    $scope.statusPageSize = 5;
    $scope.statusLimit = 5;
    $scope.statusOffset = 0;

    $scope.reloadStatuses = function() {
        var params = {
            'limit': $scope.statusLimit,
            'offset': $scope.statusOffset,
            'ordering': $scope.statusSortType,
            'project': $routeParams.id,
        }

        var error_func = function (resp) {console.log(resp);};

        if (!$scope.statusLimit) {
            projectStatusService.get_all(
                params,
                function(resp) {
                    $scope.statuses = resp;
                },
                error_func
            )
        } else {
            projectStatusService.get(
                params,
                function(resp) {
                    $scope.statuses = resp.results;
                },
                error_func
            )
        }
    };

    $scope.statusSortVariants = [
        {title: "by Name Asc", type: 'name'},
        {title: "by Name Desc", type: '-name'},
        {title: "by Order Number Asc", type: 'order_number'},
        {title: "by Order Number Desc", type: '-order_number'}
    ];
    $scope.viewStatusVariants = ["5", "10", "20", "50", "All"];

    $scope.statusSort = function(sortInfo) {
        $scope.statusSortType = sortInfo.type;
        $scope.statusPage = 1;
        $scope.reloadStatuses();
    };

    $scope.viewStatus = function(viewInfo) {
        if (viewInfo === 'All') {
            $scope.statusLimit = '';
        } else {
            $scope.statusLimit = viewInfo;
        }
        $scope.statusPage = 1;
        $scope.reloadStatuses();
    };

    $scope.reloadStatuses();

    // Add Status
    $scope.showAddStatusDialog = function(event) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'add_status.tmpl.html',
            parent: angular.element(document.body),
            targetEvent: event,
            scope: $scope,
            preserveScope: true,
            clickOutsideToClose: true,
            fullscreen: false
        });
    };

    // Delete status
    $scope.deleteStatusPopup = function(ev, id, name) {
        var confirm = $mdDialog.confirm()
              .title('Would you like to delete status?')
              .textContent('Are you sure you mant to delete status ' + name + "?")
              .ariaLabel('Lucky day')
              .targetEvent(ev)
              .ok('Delete')
              .cancel('Cancel');

        $mdDialog.show(confirm).then(
            function() {
                projectSelectedStatusService.remove_status(
                    {id: id}, {},
                    function(resp) {
                        $scope.reloadStatuses();
                    },
                    function(resp) {
                        $log.debug(
                            "Status: " + resp.status + " Status text: " + resp.statusText + " Detail: " + resp.data.detail
                        );
                    }
                )
            }
        );
      };

    // Edit status

    $scope.viewSelectedStatus = function (ev, id) {
        $location.url('/user/status/' + id);
    };

    // TAG manipulations
    $scope.searchTag = function(tag) {
        $location.url('/user/projects/tag/' + tag.name);
    };

    $scope.addTag = function(tag) {
        project_tagService.add_tag(
            {'id': $routeParams.id, 'tag_name': tag.name}, {}, function(response) {
            }, function () {
                $scope.project.tags.splice($scope.project.tags.length - 1, 1);
            }
        );
    };

    $scope.removeTag = function(tag) {
        tag_name = tag.name;

        project_tagService.delete_tag(
            {'id': $routeParams.id, 'tag_name': tag_name}, {}, function(response) {
            }, function () {
                $scope.project.tags.push(tag);
            }
        );
    };

    $scope.newTag = function(tag) {
        return {'name': tag};
    };

    /* ACTIVITY INFO */
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
            'ordering': sorting,
            'project_activities': $routeParams.id
        }

        activityListService.get(params, function (data) {
            $scope.activities = {}
            $scope.activities.data = data.results;
            $scope.activities.count = $scope.activities.data.length;
            console.log($scope.activities.data);
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
            'for_cu':1,
            'project_activities': $routeParams.id
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
    $scope.taskPageSize = 10;
    $scope.taskPage = 1;

    $scope.viewTaskVariants = ["5", "10", "20", "50", "All"];

    $scope.taskSortVariants = [
        {title: "by Title Asc", type: 'name', direction: true},
        {title: "by Title Desc", type: 'name', direction: false},
        {title: "by Status Asc", type: 'status', direction: true},
        {title: "by Status Desc", type: 'status', direction: false}
    ];

    var reloadTask = function() {
        var sorting = ($scope.taskSortDirection ? '' : '-') + $scope.taskSortType;
        var params = {
            'page': $scope.taskPage,
            'page_size': $scope.taskPageSize,
            'ordering': sorting,
            'for_cu':1,
            'project': $routeParams.id
        }

        taskService.get(params, function (data) {
            $scope.tasks = {}
            $scope.tasks.data = data.results;
            $scope.tasks.count = $scope.tasks.data.length;
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

    $scope.sortVariants = [
          {value: "created_at",
           option: "by Date"
          },
          {value: "created_by",
           option: "by User"
          },
//          {value: "comment",
//           option: "by Type"
//          },
      ];



    reloadTask();

    /* COMMENT */
    $scope.commentSortType = 'created_at'; // set the default sort type
    $scope.commentSortDirection = true;  // set the default sort order
    $scope.commentPageSize = 10;
    $scope.commentPage = 1;

    $scope.viewCommentVariants = ["5", "10", "20", "50", "All"];

    var reloadComment = function() {
        var sorting = ($scope.commentSortDirection ? '' : '-') + $scope.commentSortType;
        var params = {
            'page': $scope.commentPage,
            'page_size': $scope.commentPageSize,
            'ordering': sorting,
            'for_cu':1,
            'project': $routeParams.id

        }
        console.log("---", params);
        commentService.get(params, function (data) {
            $scope.comments = data.results;
            $scope.comments.count = $scope.comments.length;
            console.log('data.results', data.results,'-----', $scope.comments.count);
        });
    };

    $scope.commentSort = function(sortInfo) {
        $scope.commentSortType = sortInfo.type;
        $scope.commentSortDirection = sortInfo.direction;
        $scope.commentPage = 1;
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

    reloadComment();


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
    }

    $scope.commentData = {};
    $scope.saveComment = function() {
//        $scope.commentData.tags = [];
        $scope.commentData.project = 'http://' + $window.location.host + '/projects/' + $routeParams.id + '/';
//        console.log('iii',$routeParams.id)
        if ($scope.comment_id) {
            // EDIT
            $scope.commentData.id = $scope.comment_id;

            commentSelectedService.update($scope.commentData, function(response) {
                $scope.commentData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/' + $routeParams.id + '/';
                }
            });
        } else {
            commentService.create($scope.commentData, function(response) {
                $scope.commentData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/' + $routeParams.id + '/';
                }
            });
        }
    };

}]);