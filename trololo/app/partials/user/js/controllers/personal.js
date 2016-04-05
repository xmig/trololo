'use strict';

var isDlgOpen;

angular.module('userApp').controller('personalCtrl', ['$scope', '$http', 'personalInfoService', '$mdToast', function ($scope, $http, personalInfoService, $mdToast) {
    $scope.userPersonalData = {};
    $scope.userAdditionData = {};
    $scope.myFile = {}

    personalInfoService.get(function (data) {
        $scope.userAdditionData = {
            first_name: data.first_name,
            last_name: data.last_name,
            department: data.department,
            specialization: data.specialization,
            detailed_info: data.detailed_info,
            use_gravatar: data.use_gravatar
        };
        $scope.userPersonalData = data;
    });

    $scope.isEmpty = function(obj) {
        return Object.keys(obj).length === 0;
    };

    $scope.compareData = function(firstObj, secondObj){
        var coincidedElementsArray = [];
        if(!$scope.isEmpty(secondObj)){
            angular.forEach(secondObj, function(svalue, skey){
                angular.forEach(firstObj, function(fvalue, fkey){
                    if(skey === fkey && svalue !== fvalue){
                        coincidedElementsArray.push(skey);
                    }
                })
            })
        }
        return coincidedElementsArray;
    };

    $scope.showPersonalToastSave = function() {
        $mdToast.show({
            hideDelay   : 3000,
            position    : 'top right',
            controller  : 'ToastCtrl',
            templateUrl : 'personal-save-template.html'
        });
    };

    $scope.showPersonalToastReject = function() {
        $mdToast.show({
            hideDelay   : 3000,
            position    : 'top right',
            controller  : 'ToastCtrl',
            templateUrl : 'personal-reject-template.html'
        });
    };

    $scope.AdditionalInfoSubmit = function(){
        if($scope.compareData($scope.userPersonalData, $scope.userAdditionData).length){
            $scope.savePersonalForm();
        } else {
            $scope.showPersonalToastReject();
        }
    };

    $scope.savePersonalForm = function () {
        personalInfoService.update($scope.userAdditionData, function(response) {
            $scope.userPersonalData = response;
             $scope.showPersonalToastSave();
        });
    };

    $scope.UserPhotoSubmit = function () {
        var fd = new FormData();
        fd.append('photo', $scope.myFile);
        fd.append('id', $scope.userPersonalData["id"]);
        personalInfoService.update_photo(fd, function(response) {
            $scope.userPersonalData = response;
            $scope.showPersonalToastSave();
        });
    };

}]);

angular.module('userApp').directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                    scope.UserPhotoSubmit();
                });
            });
        }
    };
}]);