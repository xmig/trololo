angular.module('userApp').controller('userCtrl', ['$scope', '$timeout', '$mdSidenav', '$log', '$routeParams', 'personalInfoService', '$window', function($scope, $timeout, $mdSidenav, $log, $routeParams, personalInfoService, $window){
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };
    $scope.partialPath = '/static/user/templates/' + $routeParams.userLocation + '.html';
    $scope.location = $routeParams.userLocation;
    console.log("$routeParams.userLocation", $routeParams.userLocation);
    console.log("$routeParams", $routeParams.id);
    $scope.userPersonalData = {};
    $scope.userAdditionData = {};
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
//    console.log("-----")
    e.preventDefault();
        if($scope.userPersonalData.id !== id){
            $window.location.href = '#/user/profile/' + id;
        } else {
            $window.location.href = '#/user/personal/';
        }
    }

///user/profile/{{task.owner.id}}
}]);
