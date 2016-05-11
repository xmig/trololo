angular.module('userApp', ['md.data.table']);

angular.module('userApp').config(['$mdThemingProvider', function ($mdThemingProvider) {
    'use strict';

    $mdThemingProvider.theme('default')
      .primaryPalette('blue');
}]);

// remain trailing slashes
angular.module('userApp').config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
});



