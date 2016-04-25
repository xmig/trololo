angular.module('userApp').controller('commentCreateCtrl', ['$scope', '$rootScope', '$http', '$window', '$mdDialog', '$mdMedia', '$routeParams', 'commentService', 'commentSelectedService',
    function($scope, $rootScope, $http, $window, $mdDialog, $mdMedia, $routeParams, commentService,commentSelectedService)
{

 console.log("----");
    $scope.comment_id = $routeParams.id;
    $scope.partialPath = '/static/user/templates/project_selected.html';

    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
        return $mdSidenav('right').isOpen();
    };

    $scope.leftSidebarList = [
        {"title": "Personal Info", "link": "personal"},
        {"title": "Projects", "link": "projects"},
        {"title": "Tasks", "link": "tasks"},
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

//    var action = $routeParams.action;
//
//    // PROJECT CALCULATE
//    projectSelectedService.get({ id: $routeParams.id }, function (data) {
//        $scope.project = data;
//    });

    $scope.commentData = {};

//    $scope.projectStatuses = [
//        {'title': 'Breakthrough', 'id':'breakthrough'},
//        {'title': 'In_progress', 'id':'in_progress'},
//        {'title': 'Finished', 'id':'finished'},
//        {'title': 'Undefined', 'id':'undefined'}
//    ];

    $scope.visibleByList = [
        {'title': 'Members', 'id':'created_by'},
//        {'title': 'Particular_user', 'id':'particular_user'},
//        {'title': 'All_users', 'id':'all_users'},
//        {'title': 'Undefined', 'id':'undefined'}

    ];

    if ($scope.comment_id) {
        // EDIT
        // PROJECT CALCULATE
        commentSelectedService.get({ id: $scope.comment_id }, function (data) {
            $scope.commentData = data;
        });
    }

    $scope.saveComment = function() {
        $scope.commentData.tags = [];
        console.log("----");

        if ($scope.comment_id) {
            // EDIT
            $scope.commentData.id = $scope.comment_id;

            commentSelectedService.update($scope.commentData, function(response) {
                $scope.commentData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/comments/' + $scope.commentData.id;
                }
            });
        } else {
            commentService.create($scope.commentData, function(response) {
                $scope.commentData = response;
                if (typeof response.id !== 'undefined' && response.id > 0) {
                    $window.location.href = '#/user/projects/comments/' + response.id + '/edit';
                }
            });
        }
    };

}])
.config(function($mdDateLocaleProvider) {
  $mdDateLocaleProvider.formatDate = function(date) {
    return date ? moment(date).format('DD-MM-YYYY') : '';
  };

  $mdDateLocaleProvider.parseDate = function(dateString) {
    var m = moment(dateString, 'DD-MM-YYYY', true);
    return m.isValid() ? m.toDate() : new Date(NaN);
  };
});