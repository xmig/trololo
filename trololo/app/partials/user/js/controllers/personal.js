angular.module('userApp').controller('personalCtrl', ['$scope', 'personalInfoService', function($scope, personalInfoService){
    $scope.userPersonalData = {};
    $scope.dublicatePersonalData = {};

    personalInfoService.get(function(data) {
        console.log("data", data);
        $scope.userPersonalData = data;
        $scope.dublicatePersonalData = angular.copy($scope.userPersonalData);
    });

    $scope.saveForm = function(){
        $scope.dublicatePersonalData.first_name = "Max"; //hardcode
        personalInfoService.update($scope.dublicatePersonalData, function(data) {
            $scope.userPersonalData = data;
        });
    };
}]);
