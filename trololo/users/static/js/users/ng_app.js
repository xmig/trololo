(function(angular){
    'use strict';

    var app = angular.module("userApp", [
        "customFilters",
        "UserSettings",
        "elif",
        "User",
        "UserRole",
        "PossibleRoles",
        "CustomerOrders"]);

    app.config(function($filterProvider) {
    });

    // Set up a template "custom brackets"
    // @see https://docs.angularjs.org/api/ng/provider/$interpolateProvider
    //---------------------------------------------------------------------
    app.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('[#').endSymbol('#]');
    });

    app.config(function($resourceProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
    });


    app.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    }]);
    window.userApp = app;
})(window.angular);

