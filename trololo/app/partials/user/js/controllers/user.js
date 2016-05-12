angular.module('userApp').controller('userCtrl', ['$scope', '$timeout', '$mdSidenav', '$log', '$routeParams', 'personalInfoService', '$window', function($scope, $timeout, $mdSidenav, $log, $routeParams, personalInfoService, $window){
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    // search by tags
    if ($routeParams.project_tag !== undefined) {
        $routeParams.userLocation = 'projects';
    } else if ($routeParams.task_tag !== undefined) {
        $routeParams.userLocation = 'tasks';
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
//    TODO: move this function it to the masterCtrl
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
        };
        $scope.userPersonalData = data;

        $scope.checkSocial = function(provider) {
            var val = false;
            console.log("User acc: " + $scope.userAdditionData.social_accounts);
            if ($scope.userPersonalData.social_accounts) {
                val = $scope.userPersonalData.social_accounts.indexOf(provider) > -1;
            }
            return val;
        };

        $scope.social_links.forEach(
            function(val, ind) {
                if ($scope.checkSocial(val.name)) {
                    $scope.social_links[ind].link = '/accounts/social/connections/';
                    $scope.social_links[ind].link_text = "UNLINK " + val.name.toUpperCase();
                } else {
                    $scope.social_links[ind].link_text = val.name.toUpperCase();
                }
            }
        )
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
