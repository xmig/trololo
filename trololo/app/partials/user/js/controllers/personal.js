angular.module('userApp').controller('personalCtrl', ['$scope', '$http', 'personalInfoService', function ($scope, $http, personalInfoService) {
    $scope.userPersonalData = {};
    $scope.userAdditionData = {};

    personalInfoService.get(function (data) {
        $scope.userAdditionData = {
            first_name: data.first_name,
            last_name: data.last_name,
            department: data.department,
            specialization: data.specialization,
            detailed_info: data.detailed_info
        };
        $scope.userPersonalData = data;
    });

    $scope.isEmpty = function(obj) {
        return Object.keys(obj).length === 0;
    };

    $scope.compareData = function(firstObj, secondObj){
        $scope.coincidedElementsArray = [];

        if(!$scope.isEmpty(secondObj)){
            angular.forEach(secondObj, function(svalue, skey){
                angular.forEach(firstObj, function(fvalue, fkey){
                    console.log("+++", svalue === fvalue);
                    if(skey === fkey && svalue !== fvalue){
                        $scope.coincidedElementsArray.push(skey);
                    }
                })
            })
        }
        console.log($scope.coincidedElementsArray);
        return $scope.coincidedElementsArray;
    };

    $scope.AdditionalInfoSubmit = function () {
        $scope.compareData($scope.userPersonalData, $scope.userAdditionData);
        personalInfoService.update($scope.userAdditionData, function(response) {
            $scope.userPersonalData = response;
        });
    };
}]);
