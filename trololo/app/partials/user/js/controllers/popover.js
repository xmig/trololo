//ui-bootstrap-for-popover

angular.module('userApp').controller('PopoverDemoCtrl', function ($scope, $sce) {

    $scope.bsPopover = {
//        content: 'Hello, World!',
        templateUrl: 'myPopoverTemplate.html',
//        title: 'Title'
    };

    $scope.placement = {
        options: [
            'top',
            'top-left',
            'top-right',
            'bottom',
            'bottom-left',
            'bottom-right',
            'left',
            'left-top',
            'left-bottom',
            'right',
            'right-top',
            'right-bottom'
        ],
        selected: 'top'
    };
});