angular.module('userApp').controller('userinfoCtrl', ['$scope', '$rootScope', '$http', 'taskService', '$mdDialog', '$mdMedia', '$routeParams', 'userService', function($scope, $rootScope, $http, taskService, $mdDialog, $mdMedia, $routeParams, userService){
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };
    $scope.partialPath = '/static/user/templates/userinfo.html';
    //$scope.location = $routeParams.userLocation;


// get all data,filter by name of selected object
    taskService.get(function (data) {
        $scope.tasks = {}
        $scope.tasks.data = data.results;
//        $scope.tasks.count = $scope.tasks.data.length;
//        console.log($routeParams)
//        console.log($scope.tasks.data)

        $scope.name = $routeParams.taskname;

        var tasks = data.results;
        $scope.task = tasks.filter(function(entry){
            return entry.name === $scope.name;
        })[0];
//        console.log(tasks)
        console.log($scope.task.activity)

    });
//


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




    // CODE
    console.log($routeParams.username)
    userService.get({"id": $routeParams.id}, function(data) {
    console.log('DATA', data);
        $scope.user = data;
        console.log("$scope.user", $scope.user1);
    }, function(error){
        console.log('DATA', error);
        window.location = '/#/404';
    });

}]);
