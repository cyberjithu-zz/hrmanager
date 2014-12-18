  hrapp.controller("chatController", function($scope, $window) {
      $scope.init = function(sender, receiver){
          $("#chatbody").animate({ scrollTop: $('#chatbody')[0].scrollHeight}, 1000);
          $scope.sender = sender;
          $scope.receiver = receiver;
          var dots = '.'
          ws_data = {'sender':$scope.sender, 'receiver': $scope.receiver};
          ws = new WebSocket("ws://192.168.0.20:8888/data="+JSON.stringify(ws_data));
          ws.onmessage = function(event) {
              var message = JSON.parse(event.data);
              if(message['typing'] == 'true'){
                dots = dots + '.';
                $(".user_typing").html(message['receiver'] + ' is typing' + dots);
                if(dots== '...')
                  dots = '';
              }
              else{
                $(".user_typing").html('');
                $("#chatbody").append('<br/><p><span class="sender">' +
                  message['sender']+'</span><span class="datetime">' +
                  message['datetime']+'</span><br/><span class="message-body">'+
                  message['message_body']+'</span></p>');
                $("#chatbody").animate({ scrollTop: $('#chatbody')[0].scrollHeight}, 1000);
              }
          };
          ws.onclose = function(event) { alert("Connection close"); };
          ws.onopen = function(event) { 
                $scope.sendMessage = function(event){
                    if(event.which == 13 && !event.shiftKey && $scope.message_body!= '') {
                        alert('aaa')
                        $("#chatbody").animate({ scrollTop: $('#chatbody')[0].scrollHeight}, 1000);
                        event.preventDefault();
                        var msg_datetime = new Date().format('M. d, Y, h:i a')
                        var message_body = $scope.message_body;
                        $scope.message_body = '';
                        $("#chatbody").append('<br/><p><span class="sender">' +
                          $scope.sender+'</span><span class="datetime">' +
                          msg_datetime+'</span><br/><span class="message-body">'+
                          message_body+'</span></p>');
                        var data = {'typing':'false' ,'message_body':message_body, 'sender':$scope.sender, 'receiver':$scope.receiver, 'datetime':msg_datetime};
                        ws.send(JSON.stringify(data));
                      }
                    else{
                        var data = {'typing':'true' ,'message_body':'', 'sender':$scope.sender, 'receiver':$scope.receiver, 'datetime':''};
                        ws.send(JSON.stringify(data));
                    }
                }; 
          };
      };
          $scope.loadMessages = function(user2){
              $window.location.href = 'user-'+user2
      };
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