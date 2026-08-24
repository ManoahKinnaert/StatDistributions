from flask import Flask, render_template
import webview 

server = Flask(__name__, static_folder="./static", template_folder="./templates")

@server.route("/")
def main():
    return render_template("index.html")


def launch_webview():
    webview.create_window("StatDistributions", server)
    webview.start() 

def launch_server_debug_mode():
    server.run(debug=True) 

if __name__ == "__main__":
    import os
    try:
        if os.environ["DEV"]:
            launch_server_debug_mode() 
        else:
            launch_webview()
    except KeyError:
        launch_webview()

    