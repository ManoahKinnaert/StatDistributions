from flask import Flask, render_template, redirect, request, jsonify
import webview 

import numpy as np 
from scipy.stats import norm, binom

server = Flask(__name__, static_folder="./static", template_folder="./templates")

@server.route("/normalDist")
def normal_dist():
    return render_template("normalDist.html")

@server.route("/binomDist")
def binom_dist():
    return render_template("binomDist.html")

@server.route("/")
def main():
    return redirect("/normalDist")

@server.route("/binom_calc")
def calculate_binom():
    # get the params
    n = int(request.args.get("n"))
    p = int(request.args.get("p"))
    # calculations for plotting pmf
    k = np.arange(0, n + 1)
    y_pmf = binom.pmf(k, n, p)
    # calculations for plotting cdf 
    y_cdf = binom.cdf(k, n, p)
    # return a json response
    return jsonify({"x": k, "y_pmf": y_pmf, "y_cdf": y_cdf})
    
@server.route("/normal_calc")
def calculate_normal():
    # get the params
    mu = float(request.args.get("mu"))
    sigma = float(request.args.get("sigma"))
    # calculate the points to be shown on the chart
    x = np.linspace(mu - 3 * sigma - .2, mu + 3 * sigma + .2, 100)
    y = norm.pdf(x, mu, sigma)
    # return a json response
    return jsonify({"x": x, "y": y})

def launch_webview():
    webview.create_window("StatDistributions", server)
    webview.start() 

def launch_server_debug_mode():
    server.run(debug=True) 

if __name__ == "__main__":
    import os
    if os.environ.get("DEV"):
        launch_server_debug_mode()
    else:
        launch_webview()

    