angular.module('userApp').controller('tasksCtrl', ['$scope', '$rootScope', '$http', 'taskService', 'activityListService', '$mdDialog', '$mdMedia', function($scope, $rootScope, $http, taskService, activityListService, $mdDialog, $mdMedia){
    taskService.get(function (data) {

console.log(data)
        $scope.tasks = {}
        $scope.tasks.data = data.results;
        $scope.tasks.count = $scope.tasks.data.length;
    });


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
            'ordering': sorting
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





    $scope.getStatuses = function () {
        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
    };

    $scope.getTypes = function () {
        return ['bug', 'feature', 'undefined'];
    };

/* end - for popup */


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

    /* Test activity data */
    $scope.my_tsks = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'assigned you to a new Task to the Project', project: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'assigned you to a new Task to the Project', project: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'assigned you to a new Task to the Project', project: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', project: 'WTF' },
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'assigned you to a new Task to the Project', project: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'assigned you to a new Task to the Project', project: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'assigned you to a new Task to the Project', project: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', project: 'WTF' }
    ];

    $scope.all_tsks = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'new Task to the Project', task: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', task: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', task: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', task: 'WTF' }
    ];

    $scope.t_activity = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'new Task to the Project', task: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', task: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', task: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', task: 'WTF' }
    ];

    $scope.my_notifications = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha-Masha', action: 'new Task to the Project', task: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', task: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', task: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', task: 'WTF' }
    ];

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


    $scope.viewVariants = [
          "5",
          "10",
          "20",
          "50",
          "All"
      ];
    /* Test activity data end */
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