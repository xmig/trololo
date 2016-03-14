(function(angular){
    'use strict';

    userApp.controller('UserSettings',
        function($scope, $filter, UserSettingsService ) {
            $scope.pageSize = clientListPageSize;

            $scope.elements = $scope.products;
            $scope.setPageSize = function (page_size) {
                var x = UserSettingsService.get({user: 1}); // 1 = 'admin' user_id
                var z = UserSettingsService.update({user: 1, type: "product_page_size", value: page_size }); // 1 = 'admin'

                console.log(x);
                console.log(z);
                $scope.pageSize = page_size
            };
        });

})(window.angular);

