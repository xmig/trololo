angular.module('userApp', ['md.data.table', 'ngMaterial', 'lfNgMdFileInput']);

angular.module('userApp').config(['$mdThemingProvider', function ($mdThemingProvider) {
    'use strict';

    $mdThemingProvider.theme('default')
      .primaryPalette('blue');
}]);

// remain trailing slashes
angular.module('userApp').config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
});



angular.module('userApp').filter('htmlrender', function(){
        return function(value) {
            var urlRegex = /(\s|^)(?:http:\/\/www\.|https:\/\/www\.|www\.)?youtube.com\/watch\?\S*v=(\S*?)(?:\s|&\S*|$)/g;
            return value.replace(urlRegex, function (url) {
                url = url.replace('watch?v=', 'embed/');
                return '<iframe width="130" height="80" src="'  + url + '" frameborder="0" allowfullscreen="true"</iframe>'
            })
        }
    });