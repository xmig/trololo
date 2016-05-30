angular.module('userApp').controller('searchCtrl', ['$scope', '$mdDialog', '$mdMedia', '$rootScope', 'searchService',
    function($scope, $mdDialog, $mdMedia, $rootScope, searchService){

    $scope.project = [];
    $scope.task = [];
    $scope.task_comment = [];

    $scope.search_text = $rootScope.searchPhrase;

    if ($rootScope.searchPhrase) {
        searchService.get(
            {search_phrase: $rootScope.searchPhrase},
            function(data) {
                $scope.project = data.project;
                $scope.task = data.task;
                $scope.task_comment = data.task_comment;
            },
            function(resp) {
                console.log("RESPONSE: ", resp);
            }
        )
    };

}]);