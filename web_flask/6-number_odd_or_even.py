#!/usr/bin/python3"""
Start a flask web application
"""
from flask import Flask, render_template

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
@app.route('/c/<path:text>', strict_slashes=False, defaults={
  'text': 'is cool'})
@app.route('/c/', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<path:text>', strict_slashes=False, defaults={
  'text': 'is cool'})
@app.route('/python/', strict_slashes=False)
def python_route(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f'{n} is a number'

# Route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n=None):
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', value=n,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
