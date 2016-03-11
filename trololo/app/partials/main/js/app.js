'use strict';

angular.module('mainApp', [
        'ngCookies',
        'ngResource',
        'ngSanitize',
        'ngRoute',
        'ngMaterial',
        'material.svgAssetsCache',
        'userApp'
    ])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/main/templates/main.html',
                controller: 'MainCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/register', {
                templateUrl: '/static/main/templates/register.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/passwordReset', {
                templateUrl: '/static/main/templates/passwordreset.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/passwordResetConfirm/:firstToken/:passwordResetToken', {
                templateUrl: '/static/main/templates/passwordresetconfirm.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/login', {
                templateUrl: '/static/main/templates/login.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/verifyEmail/:emailVerificationToken', {
                templateUrl: '/static/main/templates/verifyemail.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/logout', {
                templateUrl: '/static/main/templates/logout.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/userProfile', {
                templateUrl: '/static/main/templates/userprofile.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/passwordChange', {
                templateUrl: '/static/main/templates/passwordchange.html',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/restricted', {
                templateUrl: '/static/main/templates/restricted.html',
                controller: 'RestrictedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/authRequired', {
                templateUrl: '/static/main/templates/authrequired.html',
                controller: 'AuthrequiredCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/:userLocation', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'userCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .otherwise({
                redirectTo: '/'
            });
    })
    .run(function (djangoAuth) {
        djangoAuth.initialize('//127.0.0.1:8000/rest-auth', false);
    });
