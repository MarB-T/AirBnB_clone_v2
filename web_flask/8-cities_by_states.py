#!/usr/bin/python3
"""
Lits/render cities by states
"""

from flask import FLask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ list/render States """
    states = storage.all('States')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """ close sql session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
