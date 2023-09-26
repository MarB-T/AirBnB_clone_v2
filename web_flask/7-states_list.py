#!/usr/bin/python3
"""
Script  to start a Flask web app and display states_list
"""

import sys
sys.path.append('/home/black/ALX-workspace/AirBnB_clone_v2')
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """render states list in storage"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """ close sql session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
