#!/usr/bin/python3
"""
4-number_route
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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    returns C with variable
    """
    text1 = text.replace("_", " ")
    return 'C {}'.format(text1)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """
    returns python with variable
    """
    text1 = text.replace("_", " ")
    return 'Python {}'.format(text1)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    return number - n
    """
    return '{} is a Number'.format(n)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
