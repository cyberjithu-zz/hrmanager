import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json


class WSHandler(tornado.websocket.WebSocketHandler):
    CONNECTIONS = []

    def open(self):
        print 'new connection'
        self.CONNECTIONS.append(self)
        print self.CONNECTIONS
        # self.write_message("Message from server")

    def on_message(self, message):
        print 'message received %s' % json.loads(message)
        self.write_message("Message from server")

    def on_close(self):
        self.CONNECTIONS.remove(self)
        print 'connection closed'


application = tornado.web.Application([
    (r'/', WSHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888, address='192.168.1.16')
    tornado.ioloop.IOLoop.instance().start()
