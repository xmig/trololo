angular.module('userApp').controller('statusSelectedCtrl', ['$scope', '$rootScope', '$window', '$mdDialog', '$mdMedia', '$routeParams', '$mdSidenav', '$timeout', '$log', 'projectSelectedStatusService', '$mdToast',
    function($scope, $rootScope, $window, $mdDialog, $mdMedia, $routeParams, $mdSidenav, $timeout, $log, projectSelectedStatusService, $mdToast)
{
    $scope.status_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/status_selected.html';

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
    };

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
    };

    function buildToggler(navID) {
        return function() {
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        }
    };

    $scope.statusData = projectSelectedStatusService.get(
        {id: $scope.status_id},
        function (data) {
            $scope.statusDataCopy = JSON.parse(JSON.stringify(data));
        }
    );

    $scope.statusSaveToast = function(text) {
        $mdToast.show(
            $mdToast.simple()
                .textContent(text)
                .position("top right")
                .hideDelay(3000)
        );
    };

    $scope.saveStatus = function() {
        if ($scope.statusDataCopy.name !== $scope.statusData.name || $scope.statusDataCopy.order_number !== $scope.statusData.order_number) {
            projectSelectedStatusService.put(
                {id: $scope.status_id},
                $scope.statusData,
                function (resp) {
                    $scope.statusDataCopy = resp;
                    $window.location = '#/user/projects/' + $scope.statusData.project_id;
                    $scope.statusSaveToast('Saved!');
                },
                function (resp) {
                    var err_message = "Error status: " + resp.status + " StatusText: " + resp.statusText;
                    $log.debug(err_message);
                    $scope.statusSaveToast('Some error, contact admin.');
                }
            )
        } else {
            $scope.statusSaveToast('Any change!');
        }
    };

}])