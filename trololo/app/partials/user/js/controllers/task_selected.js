angular.module('userApp').controller('task_selectedCtrl', ['$scope', '$rootScope', '$http', 'task_selectedService', '$mdDialog', '$mdMedia', '$routeParams', '$timeout', '$mdSidenav', 'task_tagService', '$log', 'personalInfoService', '$window', function($scope, $rootScope, $http, task_selectedService, $mdDialog, $mdMedia, $routeParams, $timeout, $mdSidenav, task_tagService, $log, personalInfoService, $window){
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };
    $scope.partialPath = '/static/user/templates/task_selected.html';

    //$scope.location = $routeParams.userLocation;

    console.log("---", $routeParams.taskid);

    task_selectedService.get({"id": $routeParams.taskid}, function(response) {
         console.log($scope.task);
         $scope.task = response;
    })

    // TAG manipulations
    $scope.addTag = function(tag) {
        task_tagService.add_tag(
            {'id': $routeParams.taskid, 'tag_name': tag.name}, function(response) {
            }, function () {
                $scope.task.tags.splice($scope.task.tags.length - 1, 1);
            }
        );
    };

    $scope.removeTag = function(tag) {
        tag_name = tag.name;

        task_tagService.delete_tag(
            {'id': $routeParams.taskid, 'tag_name': tag_name}, function(response) {
            }, function () {
                $scope.task.tags.push(tag);
            }
        );
    };

    $scope.newTag = function(tag) {
        return {'name': tag};
    };

//// get all data,filter by name of selected object
//    taskService.get(function (data) {
//        $scope.tasks = {}
//        $scope.tasks.data = data.results;
////        $scope.tasks.count = $scope.tasks.data.length;
////        console.log($routeParams)
////        console.log($scope.tasks.data)
//
//        $scope.name = $routeParams.taskname;
//
//        var tasks = data.results;
//        $scope.task = tasks.filter(function(entry){
//            return entry.name === $scope.name;
//        })[0];
////        console.log(tasks)
//        console.log($scope.task.activity)
//
//    });
////


    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
        //{"title": "Progress", "link": "progress"},
        //{"title": "Teams", "link": "teams"},
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



    $scope.getStatuses = function () {
        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
    };

    $scope.getTypes = function () {
        return ['bug', 'feature', 'undefined'];
    };

/* end - for popup */

//angular.module('userApp').controller('tasksCtrl', ['$scope', function($scope){



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


    $scope.my_notifications = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'new Task to the Project', task: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', task: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', task: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', task: 'WTF' }
    ];

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

    $scope.viewVariants = [
          "5",
          "10",
          "20",
          "50",
          "All"
      ];



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

}]);


///* for popup */
//function DialogController($scope, $mdDialog) {
//  $scope.hide = function() {
//    $mdDialog.hide();
//  };
//
//  $scope.cancel = function() {
//    $mdDialog.cancel();
//  };
//
//  $scope.answer = function(answer) {
//    $mdDialog.hide(answer);
//  };
//}
///* end - for popup */