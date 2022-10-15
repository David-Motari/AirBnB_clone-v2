#!/usr/bin/python3
"""
0-hello_route
starts a Flask web application
"""
from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello():
    """
    returns message
    """
    return ("Hello HBNB!")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
