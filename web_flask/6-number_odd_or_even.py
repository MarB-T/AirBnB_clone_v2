#!/usr/bin/python3
"""
script to start a Flask web App
"""

from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Display Hello HBNH! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display C followed by the value of the text variable """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """ Dispaly given text or 'is cool' if not provided """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def num_route(n):
    """ Display only if n is integer """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def num_temp(n):
    """ Render 5-number.hmtl only if n is integer """
    try:
        n = int(n)
        return render_template("5-number.html", n=n)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_even(n):
    """ Render hmtl only if n is int and show if its odd or even """
    try:
        n = int(n)
        return render_template("6-number_odd_or_even.html", n=n)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
