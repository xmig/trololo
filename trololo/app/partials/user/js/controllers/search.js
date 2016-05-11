angular.module('userApp').controller('searchCtrl', ['$scope', '$mdDialog', '$mdMedia', '$rootScope', 'searchService',
    function($scope, $mdDialog, $mdMedia, $rootScope, searchService){

    $scope.search_results = {
        project: [],
        task: [],
        task_comment: []
    };

    if ($rootScope.searchPhrase) {
        searchService.get(
            {search_phrase: $rootScope.searchPhrase},
            function(data) {
                $scope.search_results = data;
            },
            function(resp) {
                console.log("RESPONSE: ", resp);
            }
        )
    };

}]);