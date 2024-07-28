#!/usr/bin/python3
"""
starts a Flask web application.
"""
from flask import Flask

# Create an instance of the Flask class
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
    Returns a simple message
    """
    return "HBNB"


# Main block to run the Flask app
if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
