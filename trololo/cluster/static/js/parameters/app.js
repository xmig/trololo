//(function (angular) {
//    'use strict';
//    var app = angular.module("parametersApp", [
//        "elif",
//        "UserSettings",
//        "ngRoute",
//        "customFilters",
//        "ngResource",
//        "utils",
//        "mgcrea.ngStrap",
//        "ngAnimate"]);
//
//    app.config(function($filterProvider) {
//    });
//
//    app.config(function ($interpolateProvider) {
//        $interpolateProvider.startSymbol('[#').endSymbol('#]');
//    });
//
//    app.config(function ($resourceProvider) {
//        $resourceProvider.defaults.stripTrailingSlashes = false;
//    });
//
//    app.config(['$httpProvider', function ($httpProvider) {
//        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//    }]);
//
//    window.parametersApp = app;
//
//})(window.angular);
