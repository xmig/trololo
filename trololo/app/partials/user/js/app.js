angular.module('userApp', ['md.data.table']);

angular.module('userApp').config(['$mdThemingProvider', function ($mdThemingProvider) {
    'use strict';
    $mdThemingProvider.theme('default')
      .primaryPalette('blue');
}]);


