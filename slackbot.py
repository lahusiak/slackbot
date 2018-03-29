import os
from slackclient import SlackClient
from tornado.ioloop import IOLoop
from tornado.web import (
    Application,
    RequestHandler,
)

DEFAULT_PORT = 8080


class SlackHandler(RequestHandler):
    def get(self):
        slack_token = os.environ["SLACKBOT_TOKEN"]
        sc = SlackClient(slack_token)

        response = sc.api_call(
            "channel.list",
            # channel="C9ZD57E8P",
            # text="Hello from Python! :tada:"
        )
        self.write(response)


def make_app():
    return Application([
        (r'/', SlackHandler),
    ])


if __name__ == '__main__':
    port = os.environ.get('PORT', DEFAULT_PORT)
    app = make_app()
    app.listen(port)
    IOLoop.instance().start()
