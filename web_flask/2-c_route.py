#!/usr/bin/python3
"""
Starts a web application.
"""
from flask import Flask
from flask import url_for
app = Flask(__name__)


# Define the route for the root URL, ensure strict_slashes is set to False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function to handle requests to the root URL ('/').
    Returns a simple greeting message.
    """
    return "Hello HBNB!"

# Define the route for the '/hbnb' URL, ensure strict_slashes is set to False


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Function to handle requests to the '/hbnb' URL.
    Returns a simple message.
    """
    return "HBNB"

# Define the route for the '/c/<text>' URL


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Function to handle requests to the '/c/<text>' URL.
    Displays "C " followed by the value of the text variable.
    Underscore symbols in text are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')


# Main block to run the Flask app
if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
