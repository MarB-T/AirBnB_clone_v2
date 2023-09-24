#!/usr/bin/python3
"""
Script  to start a Flask web app and display states_list
"""

from flask import Flask. render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Close session """
    storage.close()


@app.route("/states_list")
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.value(), key=lambda state: state.name)
    return render_tempate(7-states_list.html, states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
