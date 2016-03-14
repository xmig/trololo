(function(angular){
    'use strict';


    userApp.controller('Users', function($scope,
                                         $filter,
                                         $timeout,
                                         UserService) {

        $scope.users = UserService.query(
            function(data) {
                console.log("Data:", data);
            }
        );
        //ng_pagginator_mixin($scope, $filter, $scope.users);
        ng_pagginator_mixin($scope, $scope.users);
        ng_tableview_mixin($scope, $scope.users, $filter);

        $scope.columns = [
            {name:'',                OrderedBy: ""},
            {name:'Full name',       OrderedBy: function(item) {return item.first_name + " " + item.last_name}},
            {name:'User name',       OrderedBy: "username"},
            {name:'Email',           OrderedBy: "email"},
            //{name:'Staff',           OrderedBy: "is_staff"},
            //{name:'Superuser',       OrderedBy: "is_superuser"},
            {name:'Active',          OrderedBy: "is_active"},
            {name:'Date joined',     OrderedBy: "date_joined"},
            {name:'Last login',      OrderedBy: "last_login"}
        ];

        $scope.prepare_sorter_data();

        $scope.usersSelected = {};

        $scope.any_selected = function() {
            return _any_selected($scope.usersSelected)
        };

        $scope.userDelSelected = function() {

            var count_for_removing = _count_selected($scope.usersSelected),
                need_to_remove = confirm("" + count_for_removing + " Customers will be Deleted");
            if (need_to_remove) {
                for (var id in $scope.usersSelected) {
                    if (! $scope.usersSelected[id]) {
                        continue;
                    }
                    UserService.delete({"id": id});
                    $("body #rowitem_" + id).notify("Deleted", "success", { position: "right middle" });
                    $timeout(function () { change_location("/users/") }, 2000);
                }
            }
        };

    });

})(window.angular);
