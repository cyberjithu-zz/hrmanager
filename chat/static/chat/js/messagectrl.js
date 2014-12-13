  hrapp.controller("chatController", function($scope, $window) {
      //ws_data = {'sender': $scope.sender, 'receiver': $scope.receiver}
      //JSON.stringify(ws_data)
      $scope.init = function(sender, receiver){
          $scope.sender = sender;
          $scope.receiver = receiver;
          ws_data = {'sender':$scope.sender, 'receiver': $scope.receiver};
          ws = new WebSocket("ws://192.168.1.3:8888/data="+JSON.stringify(ws_data));
          ws.onmessage = function(event) {
              var message = JSON.parse(event.data);
              $("#chatbody").append("<p><span class=sender>" +message['sender']+'</span>: '+message['message_body']+"</p>");
          };
          ws.onclose = function(event) { alert("Connection close"); };
          ws.onopen = function(event) { 
                $scope.sendMessage = function(event){
                    if(event.which == 13) {
                        event.preventDefault();
                        var message_body = $scope.message_body;
                        $scope.message_body = '';
                        $("#chatbody").append("<p><span class=sender>" +$scope.sender+'</span>: '+message_body+"</p>");
                        var data = {'message_body':message_body, 'sender':$scope.sender, 'receiver':$scope.receiver, 'datetime':new Date().toLocaleString()};
                        ws.send(JSON.stringify(data));
                   }; 
                };
              };
          $scope.loadMessages = function(user2){
              $window.location.href = 'user-'+user2
      };
    }
  });
/*
          alert(user2);
          $rootScope.receiver = user2;
          var request = $http({
              method: "POST",
              headers: {'X-CSRFToken':$('input[name=csrfmiddlewaretoken]').val()},
              url: "ajaxmessage/",
              data:{'user1': $scope.user1, 'user2':user2}
              });
          request.success(
              function(data) {
                  alert(data['messages'][0]['sender']);
                  $("#chatbody").html('');
                  for (var i = data['messages'].length - 1; i >= 0; i--) {
                      $("#chatbody").append("<p><span class=sender>" +data['messages'][i]['sender']+'</span>: '+data['messages'][i]['message_body']+"</p>");
                  };
              }
          );
*/