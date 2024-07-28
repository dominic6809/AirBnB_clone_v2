#!/usr/bin/python3
"""
Starst a flask web application.
"""
from flask import Flask, render_template_string

# Create a new Flask application
app = Flask(__name__)

# Route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"

# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"

# Route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of the text variable,
    with underscores replaced by spaces"""
    return f"C {text.replace('_', ' ')}"

# Route for /python/(<text>)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces.
    The default value of text is 'is cool'"""
    return f"Python {text.replace('_', ' ')}"

# Route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return f"{n} is a number"

# Route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n=None):
    return render_template_string('5-number.html', n=n)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
