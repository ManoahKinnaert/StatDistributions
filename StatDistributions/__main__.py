from flask import Flask, render_template
import webview 

server = Flask(__name__, static_folder="./static", template_folder="./templates")

@server.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    webview.create_window("StatDistributions", server)
    webview.start()