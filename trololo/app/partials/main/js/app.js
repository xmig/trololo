'use strict';

angular.module('mainApp', [
        'ngCookies',
        'ngResource',
        'ngSanitize',
        'ngRoute',
        'ngMaterial',
        'ngMessages',
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
            .when('/user/profile/:id', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'userinfoCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/404', {
                templateUrl: '/static/user/templates/404_not_found.html',
                controller: 'MainCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })

//            .when('/search/', {
//                templateUrl: '/static/user/templates/user.html',
//                controller: 'userCtrl',
//                resolve: {
//                    authenticated: ['djangoAuth', function (djangoAuth) {
//                        return djangoAuth.authenticationStatus(true);
//                    }]
//                }
//            })

            .when('/user/tasks/create', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskCreateCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/tasks/:id/edit', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskCreateCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/tasks/:taskid', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })



            .when('/user/tasks/comments/create', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })

            .when('/user/tasks/comments/:id/edit', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })

            .when('/user/tasks/comments/:id', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'taskSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })

//            .when('/user/tasks/:id', {
//                templateUrl: '/static/user/templates/user.html',
//                controller: 'taskSelectedCtrl',
//                resolve: {
//                    authenticated: ['djangoAuth', function (djangoAuth) {
//                        return djangoAuth.authenticationStatus(true);
//                    }]
//                }
//            })






             .when('/user/projects/comments/create', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/create', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectCreateCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/comments/:id/edit', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/comments/:id', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/tag/:project_tag', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'userCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/tasks/tag/:task_tag', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'userCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/:id/edit', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectCreateCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/projects/:id', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'projectSelectedCtrl',
                resolve: {
                    authenticated: ['djangoAuth', function (djangoAuth) {
                        return djangoAuth.authenticationStatus(true);
                    }]
                }
            })
            .when('/user/status/:id', {
                templateUrl: '/static/user/templates/user.html',
                controller: 'statusSelectedCtrl',
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
    .run(function (djangoAuth, $window) {
        djangoAuth.initialize('//' + $window.location.host + '/rest-auth', false);
    });

angular.module('mainApp').config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
});