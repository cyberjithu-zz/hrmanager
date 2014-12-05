  hrapp.controller("messageCtrl", function($scope) {
      ws = new WebSocket("ws://192.168.1.4:8888");
      ws.onmessage = function(event) {
          $("#chatbody").append("<p>"+event.data+"</p>");
      };
      ws.onclose = function(event) { alert("Connection close"); };
      ws.onopen = function(event) { 
            $scope.sendMessage = function(event){
                if(event.which == 13) {
                    event.preventDefault();
                    var message_body = $scope.message_body;
                    var sender = $scope.sender;
                    $scope.message_body = '';
                    $("#chatbody").append("<p><span class=sender>" +sender+'</span>: '+message_body+"</p>");
                    var data = {'message_body':message_body, 'sender':sender};
                    ws.send(JSON.stringify(data));
               };   
            };
          };
      });
