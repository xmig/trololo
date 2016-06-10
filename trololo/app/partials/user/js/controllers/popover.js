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



////POPOVER
//angular.module('userApp').controller('PopoverDemoCtrl', function ($scope, $popover) {
//
//  $scope.popover = {title: 'Title', content: 'Hello Popover<br />This is a multiline message!'};
//
//  var asAServiceOptions = {
//    title: $scope.popover.title,
//    content: $scope.popover.content,
//    trigger: 'manual'
//  }
//
//  var myPopover = $popover(angular.element(document.querySelector('#popover-as-service')), asAServiceOptions);
//  $scope.togglePopover = function() {
//    myPopover.$promise.then(myPopover.toggle);
//  };
//});





