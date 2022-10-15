#!/usr/bin/python3
"""
1-hbnb_route
starts a Flask web application
"""
from flask import Flask
import os
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns Hello HBNB!
    """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns HBNB
    """
    return ("HBNB")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

