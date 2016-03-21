angular.module('userApp').controller('personalCtrl', ['$scope', '$http', 'personalInfoService', '$cookies', function ($scope, $http, personalInfoService, $cookies) {
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

    //$scope.compareData = function(originalObj, copyObj, partObj){
    //    if(partObj.length){
    //        angular.forEach(partObj, function(elem){
    //            angular.forEach(copyObj, function(el){
    //                if(elem !== el){
    //                    el = elem;
    //                }
    //            })
    //        })
    //    }
    //    console.log("copyObj", copyObj);
    //    console.log("partObj", partObj);
    //};

    $scope.AdditionalInfoSubmit = function () {
        personalInfoService.update($scope.userAdditionData, function(response) {
            $scope.userPersonalData = response;
        });
    }
}]);
