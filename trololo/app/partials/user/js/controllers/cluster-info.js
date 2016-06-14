angular.module('userApp').controller('clusterCtrl', ['clusterInfoService', '$scope', '$timeout', '$mdSidenav',
                                                     '$log', '$routeParams', 'clusterService', '$window', '$mdDialog',
                                                     'Validate','$location','$http',
 function(clusterInfoService, $scope, $timeout, $mdSidenav, $log, $routeParams, clusterService, $window, $mdDialog, Validate, $location, $http){
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
    $scope.userPersonalData = {};
    $scope.userAdditionData = {};
    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
        {"title": "Cluster", "link": "system"},
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
    clusterService.get(function(response){

        $scope.cluster = {};
        $scope.cluster.response = response.results;
        $scope.cluster.count = $scope.cluster.response.length;
        $scope.clusterCopy = $scope.cluster;

        console.log("response", $scope.cluster.in_cluster );
    })


    $scope.showAddHostDialog = function(event) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'add_host.tmpl.html',
            parent: angular.element(document.body),
            targetEvent: event,
            scope: $scope,
            preserveScope: true,
            clickOutsideToClose: true,
            fullscreen: false
        });
    };

    $scope.addHost = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);

      if(!formData.$invalid) {
        clusterService.create(
            {
                'host_ip': $scope.host_ip,
                'hostname': $scope.host_name,
                'internal_ip': $scope.host_internal,
                'in_cluster': $scope.host_incluster,
                'enabled': $scope.host_enabled,
            }
        ).$promise
        .then(function(resp) {
            $scope.hide();
            var alert = $mdDialog.alert()
                .title('Complete')
                .textContent('Host was added!')
                .ok('Close');
            $mdDialog.show(alert)
                .finally(function() {
                    alert = undefined;
                    $scope.cluster.response.push(resp);
                });
            }, function(resp) {
                $scope.hide();

                if(resp.status !== 200) {
                    var err = $mdDialog.alert()
                        .title('Failure')
                        .htmlContent($scope.getErrorText(resp))
                        .ok('Close');
                    $mdDialog.show(err)
                        .finally(function() {
                            alert = undefined;
                        });
                }
            })
        }
    }

    $scope.viewSelectedHost = function (ev, id) {
        console.log("ID::::", id)
        $location.url('/system/' + id);
    }

    $scope.changeClusterStatus = function(index, item){
        console.log(!item.enabled);
        clusterInfoService.update({"id": item.id}, $scope.cluster.response[index], function(resp){
            console.log("done", resp,item.id);
            $scope.statusSaveToast('Saved!');
        }, function(err){
            console.log("error", err);
        });
    }

    $scope.deleteClusterPopup = function(ev, id, name) {
        console.log("Delete:::::",ev, id, name)
        var confirm = $mdDialog.confirm()
              .title('Would you like to delete host?')
              .textContent('Are you sure you mant to delete host ' + name + "?")
              .ariaLabel('Lucky day')
              .targetEvent(ev)
              .ok('Delete')
              .cancel('Cancel');

        $mdDialog.show(confirm).then(
            function() {
                clusterInfoService.delete(
                    {id: id}, {},
                    function(resp) {
//                    console.log("resp::::",resp.id )
                        $scope.cluster.response.pop(resp);
                    },
                    function(resp) {
                        $log.debug(
                            "Status: " + resp.status + " Status text: " + resp.statusText + " Detail: " + resp.data.detail
                        );
                    }
                )
            }
        );
    }

    $scope.toggleActive = function(index, check_url) {
        console.log("index:::::", index, check_url)
        $http({
            method: 'GET',
            url: check_url + '/system/health_check/',
            timeout: 2500,
        }).then(function successCallback(response) {
            angular.element($(document.querySelectorAll(".test-btn")[index]).removeClass('btn-danger').addClass('btn-success'))
        }, function errorCallback(response) {
            console.log("timeout:::",$http.timeout)
                angular.element($(document.querySelectorAll(".test-btn")[index]).removeClass('btn-success').addClass('btn-danger'))
            }
        )};
}]);

angular.module('userApp').controller('hostCtrl', ['$rootScope', 'clusterInfoService', '$scope', '$timeout', '$mdSidenav', '$log', '$routeParams', 'clusterService', '$window', '$mdDialog', 'Validate', '$filter', function($rootScope,clusterInfoService, $scope, $timeout, $mdSidenav, $log, $routeParams, clusterService, $window, $mdDialog, Validate, $filter){

    $scope.host_id = $routeParams.id
    $scope.partialPath = '/static/user/templates/host_edit.html';



    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
        {"title": "Cluster", "link": "system"},
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

    $scope.hostData = clusterInfoService.get(
        {id: $scope.host_id},
        function (data) {
            $scope.statusHostCopy = JSON.parse(JSON.stringify(data));
            console.log("DataCopy:",$scope.statusHostCopy )
        }
    );

    $scope.saveHost = function(elem) {
        if (elem.$valid == true){
            if ($scope.statusHostCopy.host_ip !== $scope.hostData.host_ip || $scope.statusHostCopy.hostname !== $scope.hostData.hostname || $scope.statusHostCopy.internal_ip !== $scope.hostData.internal_ip || $scope.statusHostCopy.in_cluster !== $scope.hostData.in_cluster || $scope.statusHostCopy.enabled !== $scope.hostData.enabled) {
                clusterInfoService.update(
                    {id: $scope.host_id},
                    $scope.hostData,
                    function (resp) {
                        $scope.statusHostCopy = resp;
                        $window.location = '#/user/system/';
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
        } else {
            $scope.statusSaveToast('Error, enter the correct data!');
        }
    };

}])