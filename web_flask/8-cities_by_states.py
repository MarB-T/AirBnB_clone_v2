#!/usr/bin/python3
"""
Lits/render cities by states
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """ close sql session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
