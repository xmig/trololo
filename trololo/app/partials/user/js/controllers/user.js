angular.module('userApp').controller('userCtrl', ['$scope', '$timeout', '$mdSidenav', '$log', '$routeParams', function($scope, $timeout, $mdSidenav, $log, $routeParams){
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.location = $routeParams.userLocation;
    $scope.partialPath = '/static/user/templates/' + $routeParams.userLocation + '.html';
    $scope.leftSidebarList = [
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
        {"title": "Progress", "link": "progress"},
        {"title": "Teams", "link": "teams"},
        {"title": "Activity", "link": "activity"},
        {"title": "Personal Info", "link": "personal"}
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
}]);
