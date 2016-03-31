angular.module('userApp').controller('projectsCtrl', ['$scope', '$http', 'projectService', function($scope, $http, projectService){
    projectService.get(function (data) {
        $scope.projects = {}
        $scope.projects.data = data.results;
        $scope.projects.count = $scope.projects.data.length;
    });

    $scope.getStatuses = function () {
        return ['breakthrough', 'in_progress', 'finished', 'undefined'];
    };




    /* Test table data */
    $scope.desserts = {
        "count": 9,
        "data": [
            {
                "name": "Frozen yogurt",
                "type": "Ice cream",
                "calories": { "value": 159.0 },
                "fat": { "value": 6.0 },
                "carbs": { "value": 24.0 },
                "protein": { "value": 4.0 },
                "sodium": { "value": 87.0 },
                "calcium": { "value": 14.0 },
                "iron": { "value": 1.0 }
            }, {
                "name": "Ice cream sandwich",
                "type": "Ice cream",
                "calories": { "value": 237.0 },
                "fat": { "value": 9.0 },
                "carbs": { "value": 37.0 },
                "protein": { "value": 4.3 },
                "sodium": { "value": 129.0 },
                "calcium": { "value": 8.0 },
                "iron": { "value": 1.0 }
            }, {
                "name": "Eclair",
                "type": "Pastry",
                "calories": { "value":  262.0 },
                "fat": { "value": 16.0 },
                "carbs": { "value": 24.0 },
                "protein": { "value":  6.0 },
                "sodium": { "value": 337.0 },
                "calcium": { "value":  6.0 },
                "iron": { "value": 7.0 }
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
            }, {
                "name": "Lollipop",
                "type": "Candy",
                "calories": { "value": 392.0 },
                "fat": { "value": 0.2 },
                "carbs": { "value": 98.0 },
                "protein": { "value": 0.0 },
                "sodium": { "value": 38.0 },
                "calcium": { "value": 0.0 },
                "iron": { "value": 2.0 }
            }, {
                "name": "Honeycomb",
                "type": "Other",
                "calories": { "value": 408.0 },
                "fat": { "value": 3.2 },
                "carbs": { "value": 87.0 },
                "protein": { "value": 6.5 },
                "sodium": { "value": 562.0 },
                "calcium": { "value": 0.0 },
                "iron": { "value": 45.0 }
            }, {
                "name": "Donut",
                "type": "Pastry",
                "calories": { "value": 452.0 },
                "fat": { "value": 25.0 },
                "carbs": { "value": 51.0 },
                "protein": { "value": 4.9 },
                "sodium": { "value": 326.0 },
                "calcium": { "value": 2.0 },
                "iron": { "value": 22.0 }
            }, {
                "name": "KitKat",
                "type": "Candy",
                "calories": { "value": 518.0 },
                "fat": { "value": 26.0 },
                "carbs": { "value": 65.0 },
                "protein": { "value": 7.0 },
                "sodium": { "value": 54.0 },
                "calcium": { "value": 12.0 },
                "iron": { "value": 6.0 }
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