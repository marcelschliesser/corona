var marcellosApp = angular.module('marcellosApp', []);

marcellosApp.controller('GetController', function ($scope, $http) {

  $scope.push = function () {
    const headers = { 'content-type': 'application/json' };

    var entry = {
      firstname: $scope.firstname,
      content: $scope.content,
      date: new Date()
    };


    const body = JSON.stringify(entry);
    console.log(body);

    $http.post("/create", body, { 'headers': headers })
      .then(function () {
        console.log('posted');
        // Todo Redirect to Homepage
      });


  };
});


marcellosApp.controller('IndexController', function ($scope, $http) {

  $http.get("/list").then(function (response) {
    console.log(response.data);
    $scope.arr = response.data;
    console.log($scope.arr);
  });



});