__version__ = "1.0.0"

from flask import Flask
from flask_cors import CORS, cross_origin
from kivy.app import App

# common modules
import signal
from multiprocessing import Process

def start_Flask():
    app.run(host="0.0.0.0", port=5000, debug=False)


def signal_handler(signal, frame):
    # for fetching CTRL+C and relatives
    exit(1)


from webview import WebView

app = Flask(__name__,
            static_folder='./static/',
            static_url_path="/ui/" # http://127.0.0.1/ui/
            )
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def catch_all(path):
    print("Launching ")
    return app.send_static_file("index.html")


class BrowserApp(App):
    def build(self):
        WebView(url = 'http://127.0.0.1:5000/ui/', enable_javascript= True)
        return None


if __name__ == "__main__":
    # print("http://127.0.0.1:5000/ui/")
    # app.run(host="0.0.0.0", port=5000, debug=False)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    global p1
    p1 = Process(target=start_Flask)    # assign Flask to a process
    p1.start()                          # run Flask as process

    BrowserApp().run()
