angular.module('userApp').controller('commentsCtrl', ['$scope', '$http', 'commentService', 'activityListService', 'taskService',
function($scope, $http, commentService, activityListService, taskService){


    /* COMMENT INFO */
    commentService.get(function (data) {
        $scope.comments = {}
        $scope.comments.data = data.results;
        $scope.comments.count = $scope.comments.data.length;
    });
}]);