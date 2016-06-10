//(function (angular) {
//    'use strict';
//    parametersApp.controller('ParametersEdit', ['$scope', 'parametersService', '$timeout', 'NotificationService', 'PaginationService', function ($scope, parametersService, $timeout, NotificationService, PaginationService) {
//        $scope.parameterslist = [];
//        $scope.parametersDetails = {};
//        $scope.parametersDetails.enabled = false;
//        NotificationService.ng_notification_mixin($scope, null, $timeout, "default");
//        //ng_notification_mixin($scope, null, $timeout, "default");
//
//        function search_parent_idxobj(categories, search_value, search_field) {
//            search_field = search_field || "name";
//            for(var index=0; index<categories.length; index++) {
//                      if(categories[index][search_field] === search_value){
//                          return [index, categories[index]];
//                      }
//            }
//            return [-1, undefined];
//        }
//        function search_parent_by_full_name(full_name) {
//            return search_parent_idxobj($scope.parameterslist, full_name, "full_name")[1];
//        }
//        function search_self_idx() {
//            return search_parent_idxobj($scope.parameterslist, $scope.parametersDetails.parameter_name)[0]
//        }
//        function search_parent_obj() {
//            return search_parent_idxobj($scope.parameterslist, $scope.parametersDetails.parent, "id")[1]
//        }
//
//        $scope.get_full_name = function() {
//            var name = $scope.parametersDetails.parameter_name,
//                parent = search_parent_obj();
//            return parent ? parent.full_name + " / " + name : name;
//
//        };
//
//        $scope.is_full_name_unique = function() {
//            var full_name = $scope.get_full_name();
//            return ! _isDefined(search_parent_by_full_name(full_name))
//        };
//
//        $scope.mode_is_created = function() {
//            return _object_is_creating($scope.parametersDetails);
//        };
//
//
//        $scope.list_update = function() {
//            var index = search_self_idx();
//            if(index !== -1) {
//                $scope.parameterslist.splice(index, 1);
//            }
//        };
//
//        $scope.init = function(id) {
//            if(_isDefined(id)) {
//               $scope.parametersDetails = parametersService.get({"id": id}, function() {
//                    console.log("parametersDetails", $scope.parametersDetails)
//                   $scope.parametersDetails.original_parameter_name = $scope.parametersDetails.parameter_name;
//                   $scope.parametersDetails.original_value = $scope.parametersDetails.value;
//                   $scope.parametersDetails.original_enabled = $scope.parametersDetails.enabled;
//
//                   $scope.parameterslist = parametersService.query(function() {
//                         $scope.list_update();
//                         $scope.parameterslist.push({ "id": null,
//                                                    "parameter_name": "",
//                                                    "value": "",
//                                                    "description": "",
//                                                    "enabled": "",
//                                                    "full_name": ""});
//                        });
//               });
//            }
//            else {
//                $scope.parameterslist = parametersService.query()
//            }
//        };
//
//        $scope.backToParameters = function() {
//            change_location("/system/parameters/");
//        };
//
//        $scope.saveNotificationOk = function(gotolocation) {
//            $scope.notification(gotolocation, "Saved!", "success");
//        };
//
//        $scope.saveNotificationError = function(data){
//            $scope.notification("","Parameter cannot be saved!", "error");
//        };
//
//        $scope.edit_mode = function() {
//            return _object_edit_mode($scope.parametersDetails);
//        };
//
//        $scope.object_not_changed = function() {
//            return ($scope.parametersDetails.original_parameter_name === $scope.parametersDetails.parameter_name)
//                && ($scope.parametersDetails.original_value === $scope.parametersDetails.value)
//                && ($scope.parametersDetails.original_description === $scope.parametersDetails.description)
//                && ($scope.parametersDetails.original_enabled === $scope.parametersDetails.enabled)
//        };
//
//        $scope.emptyFieldNotification = function(){
//            $scope.notification("","Parameters name is not defined!");
//        };
//
//        $scope.createParameters = function(success_method, error_method) {
//
//            success_method = success_method || function(data) { $scope.saveNotificationOk(null) };
//            error_method  =  error_method   || function(data) { $scope.saveNotificationError(data) };
//
//            var data = {
//                   "parameter_name":    $scope.parametersDetails.parameter_name,
//                   "value":             $scope.parametersDetails.value,
//                   "description":       $scope.parametersDetails.description,
//                   "enabled":           $scope.parametersDetails.enabled
//            };
//            console.log("WTF", $scope.parametersDetails.enabled)
//            if (! $scope.is_full_name_unique()) {
//                $scope.notification("", "Full Parameters name already defined!", "error");
//                return;
//            }
//
//            parametersService.create(data, success_method, error_method);
//        };
//
//
//        $scope.updateParameters = function(gotourl) {
//            if (! $scope.if_something_was_changed(gotourl)) {
//                return
//            }
//
//            var data = {
//                   "id":        $scope.parametersDetails.id,
//                   "parameter_name":      $scope.parametersDetails.parameter_name,
//                   "value":    $scope.parametersDetails.value,
//                   "description":    $scope.parametersDetails.description,
//                   "enabled":    $scope.parametersDetails.enabled
//            };
//            parametersService.update(data, function() {$scope.saveNotificationOk(gotourl)});
//        };
//
//
//        $scope.if_something_was_changed = function(gotolocation) {
//            if ( $scope.object_not_changed()) {
//                $scope.notification(gotolocation, "Any update", "warning");
//                return false;
//            }
//            return true;
//        };
//        /*
//        * Event Handler
//        * */
//        $scope.saveAndContinueEdit = function() {
//            if (_isDefined($scope.parametersDetails.id)) {
//                $scope.updateParameters("/system/parameters/" + $scope.parametersDetails.id + "/")
//            }
//            else {
//                $scope.createParameters(function(data) {
//                    $scope.saveNotificationOk("/system/parameters/" + data.id + "/");
//                    return data.id;
//                }, null)
//            }
//
//        };
//
//        /*
//        * Event Handler
//        * Check if Redirect need to be Updated or Created
//        * */
//        $scope.saveAndExit = function() {
//
//            if (!_isDefined($scope.parametersDetails.id)) {
//                $scope.createParameters(function () {
//                    $scope.saveNotificationOk("/system/parameters/");
//                }, null)
//
//            }
//            else {
//                $scope.updateParameters("/system/parameters/");
//            }
//        };
//
//        /*
//        * Event Handler
//        * */
//        $scope.saveAddNew = function() {
//            if (_isDefined($scope.parametersDetails.id)) {
//                $scope.updateParameters("/system/parameters/add/")
//            }
//            else {
//                $scope.createParameters(function() {
//                    $scope.saveNotificationOk("/system/parameters/add/");
//                }, null)
//            }
//        };
//
//       /*
//        * Event Handler
//        * */
//        $scope.delParameters = function() {
//            var count_of_products = $scope.parametersDetails.count_of_products;
//            if (_isDefined(count_of_products)
//                && count_of_products > 1) {
//                $scope.notification("", "This Parameters cannot be removed \n because "
//                    + count_of_products + " Products belong to it", "error");
//            }
//            else {
//                parametersService.delete({"id": $scope.parametersDetails.id});
//                $scope.notification("/system/parameters/", "Deleted", "warning");
//            }
//        };
//
//        $scope.edit_cancel = function(gotourl) {
//            gotourl = gotourl || "/system/parameters/";
//            if ( ! $scope.object_not_changed()) {
//                $scope.notification(gotourl, "Your update wasn't performed", "warning");
//            }
//            else {
//                change_location(gotourl);
//            }
//        };
//    }]);
//})(window.angular);
