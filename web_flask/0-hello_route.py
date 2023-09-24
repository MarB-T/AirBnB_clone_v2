#!usr/bin/python3
"""
script to start a Flask web App
"""

from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Display Hello HBNH! """
    return ("<p>Hello HBNB!</p>")
