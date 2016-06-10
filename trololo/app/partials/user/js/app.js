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
            var width = 130,
	            height =  80;
            var urlRegex = /(\s|^)(?:http:\/\/www\.|https:\/\/www\.|www\.)?youtube.com\/watch\?\S*v=(\S*?)(?:\s|&\S*|$)/g;
            var youtube = '$1<object width="'
			+ width
			+ '" height="'
			+ height
			+ '"><param name="movie" value="http://www.youtube.com/v/$2?version=3&amp;hl=ru_RU"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/$2?version=3&amp;hl=ru_RU" type="application/x-shockwave-flash" width="'
			+ width
			+ '" height="'
			+ height
			+ '" allowscriptaccess="always" allowfullscreen="true"></embed></object>'
//            return value.replace(urlRegex, function (url) {
//                url = url.replace('watch?v=', 'embed/');
//
//                return '<iframe width="130" height="80" src="'  + url + '" frameborder="0" allowfullscreen="true"</iframe>'
//            })
        console.log("youtube", youtube);
        return value.replace(urlRegex, youtube);
        }
    });