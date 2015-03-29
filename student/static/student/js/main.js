angular.module('mainApp', [])
    .controller('StudentListController', function($scope) {
        $scope.studentList = [
            {text:'student1', done:true},
            {text:'student2', done:false}
        ];
    });
