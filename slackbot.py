import os
from tornado.ioloop import IOLoop
from tornado.web import (
    Application,
    RequestHandler,
)

DEFAULT_PORT = 8080


class SlackHandler(RequestHandler):
    def get(self):
        self.write(“It works!”)


def make_app():
    return Application([
        (r’/’, SlackHandler),
    ])


if __name__ == ‘__main__’:
    port = os.environ.get(‘PORT’, DEFAULT_PORT)
    app = make_app()
    app.listen(port)
    IOLoop.instance().start()
