angular.module('userApp').controller('tasksCtrl', ['$scope', '$http', 'taskService', function($scope, $http, taskService){
    taskService.get(function (data) {
        $scope.tasks = {}
        $scope.tasks.data = data.results;
        $scope.tasks.count = $scope.tasks.data.length;
    });

    $scope.getStatuses = function () {
        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
    };



//angular.module('userApp').controller('tasksCtrl', ['$scope', function($scope){

    /* Test table data */
    $scope.desserts = {
        "count": 9,
        "data": [
            {
                "name": "Fifty yogurt",
                "type": "Ice cream",
                "calories": { "value": 159.0 },
                "fat": { "value": 6.0 },
                "carbs": { "value": 24.0 },
                "protein": { "value": 4.0 },
                "sodium": { "value": 87.0 },
                "calcium": { "value": 14.0 },
                "iron": { "value": 1.0 }
            }, {
                "name": "Cupcake",
                "type": "Pastry",
                "calories": { "value":  305.0 },
                "fat": { "value": 3.7 },
                "carbs": { "value": 67.0 },
                "protein": { "value": 4.3 },
                "sodium": { "value": 413.0 },
                "calcium": { "value": 3.0 },
                "iron": { "value": 8.0 }
            }, {
                "name": "Jelly bean",
                "type": "Candy",
                "calories": { "value":  375.0 },
                "fat": { "value": 0.0 },
                "carbs": { "value": 94.0 },
                "protein": { "value": 0.0 },
                "sodium": { "value": 50.0 },
                "calcium": { "value": 0.0 },
                "iron": { "value": 0.0 }
            }
        ]
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
                input.$setValidity('task_test', input.$modelValue !== 'task_test');
            });
        });
    };

    $scope.getTypes = function () {
        return ['Candy', 'Ice cream', 'Other', 'Pastry'];
    };
    /* Test table data end */

    /* Test activity data */
    $scope.toppings = [
        { name: 'Customers Import from Shopify, Customers missing in Nucleus', wanted: true, status: 'low', user: 'Masha', action: 'new Task to the Project', task: 'Villabajo' },
        { name: 'Billing', wanted: false, status: 'high', user: 'Sergey', action: 'new Task to the Project', task: 'Villaribo' },
        { name: 'Markup for tasks page 5 s/p', wanted: true, status: 'high', user: 'Masha', action: 'new Task to the Project', task: 'Trololo' },
        { name: 'Markup for projects page 5 s/p', wanted: false, status: 'middle', user: 'Max', action: 'added comment to your reply', task: 'WTF' }
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