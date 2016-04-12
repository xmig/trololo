angular.module('userApp').controller('projectsCtrl', ['$scope', '$http', 'projectService', 'activityListService', 'taskService',
function($scope, $http, projectService, activityListService, taskService){
    projectService.get(function (data) {
        $scope.projects = {}
        $scope.projects.data = data.results;
        $scope.projects.count = $scope.projects.data.length;
    });

    activityListService.get(function (data) {
        $scope.activities = {}
        $scope.activities.data = data.results;
        $scope.activities.count = $scope.activities.data.length;
    });

    activityListService.get({'for_cu':1}, function (data) {
        $scope.notifications = {}
        $scope.notifications.data = data.results;
        $scope.notifications.count = $scope.notifications.data.length;
    });

    taskService.get(function (data) {
        $scope.tasks = {}
        $scope.tasks.data = data.results;
        $scope.tasks.count = $scope.tasks.data.length;
    });

    $scope.getStatuses = function () {
        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
    };

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
                input.$setValidity('test', input.$modelValue !== 'test');
            });
        });
    };

    $scope.getTypes = function () {
        return ['Candy', 'Ice cream', 'Other', 'Pastry'];
    };
    /* Test table data end */

    /* Test activity data */
    $scope.toppings = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha', action: 'new Task to the Project', project: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', project: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', project: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', project: 'WTF' }
    ];

    $scope.sortVariants = [
          "by Date",
          "by Project",
          "by Type",
          "by Label",
          "by Status"
      ];

    $scope.viewVariants = [
          "10",
          "20",
          "50",
          "All"
      ];
    /* Test activity data end */
}]);