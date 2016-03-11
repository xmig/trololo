(function(angular) {
    'use strict';

    var empty_user_role = function(possible_roles) {
        var all_user_role = [];

        for (var i = 0; i < possible_roles.length; i++) {
            var dummy_user_role = {
                            user: "",
                            role: possible_roles[i],
                            flag: true};

            all_user_role.push(dummy_user_role)
        }
        return all_user_role
    };

// Role Item Example
//        {
//            "id": 67,,
//            "user": 15,
//            "role": {
//                "id": 1,
//                "role": "product.product.create"
//            },
//            "flag": true
//        },

    var reformat_user_roles = function(roles) {
//         for (var z=0; z<roles.length; z+=1) {
//             console.log(roles[z].role)
//         }
//        console.log("roles----", roles);
        var listMenuData = [ {
                            title: 'Shop',
                            items: ['orders', 'customers', 'subscriptions', 'subscription_plan']
                            },
                            {
                               title: 'Shipping',
                               items: ['shipping_rules', 'shipping_orders', 'shipping_batches']
                           },
                            {
                               title: 'Admin',
                               items: ['product', 'types', 'categories', 'discounts', 'users', 'pages_content']
                           },
                           {
                               title: 'Inventory',
                               items: ['log', 'modify', 'inventory_log']
                           },
                           {
                               title: 'System',
                               items: ['logs', 'memcache', 'info', 'cluster']
                           }
//                           {
//                               title: 'Business',
//                               items: ['info']
//                           }
                        ];
        var result = [];
        var tmp = {};
        var result_list =  [{'title': 'Shop', items: []},
                            {'title': 'Shipping', items: []},
                            {'title': 'Admin', items: []},
                            {'title': 'Inventory', items: []},
                            {'title': 'System', items: []}];
//                            {'title': 'Business', items: []}];

        for (var i=0; i<roles.length; i+=1) {
            var item = roles[i],
                role_name = item.role.role,
                parts = role_name.split("."),
                group = parts[0],
                base = parts[1],
                permission = parts[2],
                selector = group + "." + base;

            //if (!_isDefined(tmp[group])) {
            //    tmp[group] = []
            //}

            if(permission == "create"){
                permission += " / edit / delete";
            }
            else {
                permission += " only";
            }

            listMenuData.forEach(function(elem){
                elem.items.forEach(function(el){
                    if(el === base){

                        result_list.forEach(function(element){
                            console.log("<" + base +  "> ###[" + element['title'] + "]  [" +  elem.title + "]###" );
                            if (element['title'] === elem.title) {
                                base = parts[1].split("_").join(" ");
                                     element['items'].push({
                                        group: group,
                                        base: base,
                                        permission: permission,
                                        item: item
                                    });
                                }
                        });

                    }
                })

            });


//            if (!_isDefined(grouped[selector])) {
//                grouped[selector] = []
//            }
//
        }

        //var groups = Object.keys(tmp);
        //for (var i=0; i <groups.length; i+=1) {
        //    result.push(tmp[groups[i]])
        //}
        //console.log(result);
        //return result;

        //console.log("result_list",  result_list);
        return result_list;
    };

    userApp.controller('UserCreate', function($scope,
                                           $filter,
                                           $timeout,
                                           UserService,
                                           UserRoleService,
                                           PossibleRolesService,
                                           CustomerOrdersService)
    {
        ng_notification_mixin($scope, null, $timeout, "default");

        $scope.selected_tab = null;
        $scope.selectedTabClass = function(group) {
            return group === $scope.selected_tab ? "active" : ""
        };

        $scope.selectTabClass = function(group) {
            $scope.selected_tab = group
        };

        $scope.isSelectTab = function(group) {
            return group === $scope.selected_tab
        };

        ng_notification_mixin($scope, $("body .notification_label"));
        $scope.user_deteil = {};

        //$scope.listMenuData = [{
        //                    title: 'shop',
        //                    items: ['orders', 'customers', 'subscriptions', 'plan']
        //                   },{
        //                       title: 'shipping',
        //                       items: ['rules', 'shipping', 'batches']
        //                   },{
        //                       title: 'admin',
        //                       items: ['product', 'types', 'categories', 'discounts', 'users']
        //                   },{
        //                       title: 'admin',
        //                       items: ['log', 'modify']
        //                   }];
        $scope.init = function(id) {
            if(_isDefined(id)) {
                //console.log('Into Users');
                UserService.get({"id": id},
                    function (data) {
                        $scope.user_deteil = data;
                        $scope.RoleGroups = reformat_user_roles($scope.user_deteil.user_role);

                        //angular.forEach($scope.RoleGroups, function(el, ind){
                        //    angular.forEach(el, function(elem, index){
                        //        angular.forEach($scope.listMenuData, function(element){
                        //            angular.forEach(element.items, function(elItems){
                        //                if(elItems === elem.base){
                        //                    console.log("-----", elItems);
                        //                    elem.section = element.title;
                        //                }
                        //            });
                        //        });
                        //    });
                        //});
                        //console.log("$scope.RoleGroups", $scope.RoleGroups);
                        //$scope.customerOrders = CustomerOrdersService.query({"id": $scope.user_deteil.id},
                        //    function(data) {console.log("Customer Orders", data)}
                        //)
                    });
            //    $scope.customerdetail = CustomersService.get({"id": id},
            //    function(date) {
            //            console.log("Customer ID:", $scope.customerdetail.id);
            //            console.log("DATA", date);
            //            $scope.customerOrders = CustomerOrdersService.query({"id": $scope.customerdetail.id},
            //                function(data) {console.log("Customer Orders", data)}
            //            )
            //    }
            //);

            }
            else {
                PossibleRolesService.query(function(data) {

                    $scope.user_deteil = {
                        password: "",
                        is_superuser: true,
                        username: "",
                        first_name: "",
                        last_name: "",
                        email: "",
                        is_staff: true,
                        is_active: true,
                        date_joined: "",
                        last_login: "",
                        groups: "",
                        user_permissions: "",
                        user_role: empty_user_role(data)
                    };
                    $scope.RoleGroups = reformat_user_roles($scope.user_deteil.user_role)
                });
            }

        };

        $scope.userPassword = "";
        $scope.user_original = {};

        $scope.permissions = function() {
            //console.log("ROLES", $scope.user_deteil.user_role);
            if($scope.user_deteil.user_role == "undefined"){
                console.log("$scope.user_deteil.user_role", $scope.user_deteil.user_role);
                return true
            }
            else{
                console.log("$scope.possible_roles", $scope.possible_roles);
                return false
            }
        };

        $scope.tugglerole = function(flag, id) {
            if(_isDefined(flag)){
                console.log("----", $scope.user_deteil);
                $scope.user_deteil.user_role.forEach(function(obj){
                    if(obj.role.id === id){
                        console.log("-----------", id);
                        obj.flag = ! obj.flag;
                    }
                });
                //$scope.user_deteil.user_role[id].flag = ! $scope.user_deteil.user_role[id].flag;
            }

        };

        $scope.checkIfRole = function(flag, id) {
           //if(_isDefined($scope.user_deteil.user_role.role[id].flag)) {
           //    return $scope.user_deteil.user_role.role[id].flag;
           //}
            var result;
             $scope.user_deteil.user_role.forEach(function(obj){
                    if(obj.role.id === id && _isDefined(obj.flag)){
                        result = obj.flag;
                        return false;
                    }
                });
            return result;
        };
        $scope.emptytugglerole = function(flag, id) {
            if(_isDefined(flag)){
                $scope.possible_roles[id-1].role = ! $scope.possible_roles[id-1].role;
            }
        };

        $scope.emptycheckIfRole = function(role, id) {
           if(_isDefined($scope.possible_roles[id-1].role)) {
               return $scope.possible_roles[id-1].role;
           }
        };

        $scope.checkIfFlag= function(flag) {
            return $scope.user_deteil[flag];
        };

        $scope.tuggleIfFlag= function(flag) {
            $scope.user_deteil[flag] = ! $scope.user_deteil[flag];
        };

        $scope.invalid_field = function(message, element) {
            return $scope.notification("", message, "error", element, 500)
        };

        $scope.object_not_changed = function() {
            return _object_was_not_changed($scope.user_deteil, $scope.user_original)
        };

        $scope.saveNotification = function(gotolocation) {
             if ($scope.object_not_changed()) {
                 $scope.notification(gotolocation, "Any update", "warning");
             }
            else {
                 $scope.notification(gotolocation, "Saved", "success");
             }
        };

        $scope.mode_is_create = function() {
            return _object_is_creating($scope.user_deteil);
        };

        $scope.edit_mode = function() {
            return _object_edit_mode($scope.user_deteil);
        };


        $scope.tosave = {};
        $scope.check_meta_data = function () {
            return  [
                    {selector: "#username",        model: "user_deteil.username", check: "text | minsize=1"},
                    {selector: "#password",        model: "user_deteil.password", check: "text"},
                    {selector: "#first_name",      model: "user_deteil.first_name",  check: "text | minsize=1"},
                    {selector: "#last_name",       model: "user_deteil.last_name", check: "text | minsize=1"},
                    {selector: "#email",           model: "user_deteil.email", check: "email | minsize=4"},
                    {selector: "#is_staff",        model: "user_deteil.is_staff"},
                    {selector: "#is_superuser",    model: "user_deteil.is_superuser"},
                    {selector: "#is_active",       model: "user_deteil.is_active"},
                    {selector: "#date_joined",     model: "user_deteil.date_joined"},
                    {selector: "#last_login",      model: "user_deteil.last_login"}
                ];
        };

        $scope.perform = function(success_method, error_method) {

            if ( ! $scope.checknotify($scope.check_meta_data())) {
                return;
            }
            success_method = success_method || function () {
                $scope.notification("", "Saved!", "success");
            };

            error_method = error_method || function () {
                $scope.notification("", "Cannot save the User!", "error");
            };


            var params = {
                "username":       $scope.user_deteil.username,
                "password":       $scope.userPassword,
                "first_name":     $scope.user_deteil.first_name,
                "last_name":      $scope.user_deteil.last_name,
                "email":          $scope.user_deteil.email,
                "is_staff":       $scope.user_deteil.is_staff,
                "is_superuser":   $scope.user_deteil.is_superuser,
                "is_active":      $scope.user_deteil.is_active,
                "date_joined":    $scope.user_deteil.date_joined,
                "last_login":     $scope.user_deteil.last_login,
                "user_role":      $scope.user_deteil.user_role
            };
            console.log("params", params);
            console.log("role", $scope.user_deteil.user_role);

            if (_isDefined($scope.user_deteil.id)) {
                params.id = $scope.user_deteil.id;
                UserService.update(params, success_method, error_method)
            }
            else {
                UserService.create(params, success_method, error_method)
            }
        };

        $scope.show_all = function(criteria){
            $scope.user_deteil.user_role = criteria
        };

        /*
        * Event Handler
        * */
        $scope.saveUserAndExit = function() {
            $scope.perform(function() {
                $scope.notification("/users/", "Saved!", "success");
            });
        };
        /*
        * Event Handler
        * */
        $scope.saveUserAndContinue = function () {
            $scope.perform(function(data) {
                if(_isDefined(data)) {
                    $scope.user_deteil.id = data.id
                }
                console.log(data);
                $scope.notification("", "Saved! You can edit it", "success");
            });
        };

        /*
        * Event Handler
        * */
        $scope.saveUserAndNew = function () {
            $scope.perform(function() {
                $scope.notification("/users/add/", "Saved!", "success");
            });

        };

        /*
        * Event Handler
        * */
        $scope.delUser = function() {
            UserService.delete({"id": $scope.user_deteil.id});
            $scope.notification("/users/", "Deleted", "warning");
        };

        /*
        * Event Handler
        * */
        $scope.edit_cancel = function () {
            change_location("/users/");
        };
     });

})(window.angular);




