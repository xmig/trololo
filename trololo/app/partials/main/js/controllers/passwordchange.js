'use strict';

angular.module('mainApp')
  .controller('PasswordchangeCtrl', function ($scope, djangoAuth, Validate, $mdDialog) {
    $scope.model = {'new_password1':'','new_password2':''};
  	$scope.complete = false;
    $scope.changePassword = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        djangoAuth.changePassword($scope.model.new_password1, $scope.model.new_password2)
        .then(function(data){
        	// success case
        	$scope.hide();
        	var alert = $mdDialog.alert()
                .title('Complete')
                .textContent('Password was changed!')
                .ok('Close');
            $mdDialog.show(alert)
                .finally(function() {
                    alert = undefined;
                });
        },function(data){
        	// error case
        	$scope.errors = data;
        });
      }
    }
  });
