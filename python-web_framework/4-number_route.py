"""
4-number_route.py
~~~~~~~~~~~~~~~~~
A Flask web application with multiple routes and URL converters.

Routes:
- /: Display "Hello HBNB!"
- /hbnb: Display "HBNB"
- /c/<text>: Display "C " followed by the value of the text variable
             (replace underscore (_) symbols with a space)
- /python/<text>: Display "Python " followed by the value of the text variable
                  (replace underscore (_) symbols with a space), with a default value "is cool"
- /number/<n>: Display "<n> is a number" only if n is an integer

Usage:
python3 4-number_route.py
"""

from flask import Flask, escape

# Create a Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/").
    
    Displays a simple greeting message "Hello HBNB!" when the root URL is accessed.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the "/hbnb" URL.
    
    Displays the message "HBNB" when the "/hbnb" URL is accessed.

    Returns:
        str: The message "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route handler for the "/c/<text>" URL.
    
    Displays "C " followed by the value of the text variable,
    replacing underscore (_) symbols with a space.

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The formatted message "C <text>"
    """
    return 'C {}'.format(escape(text).replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route handler for the "/python/<text>" URL.
    
    Displays "Python " followed by the value of the text variable,
    replacing underscore (_) symbols with a space. If no text is provided,
    it uses the default value "is cool".

    Args:
        text (str): The text variable from the URL.

    Returns:
        str: The formatted message "Python <text>"
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route handler for the "/number/<n>" URL.
    
    Displays "<n> is a number" only if n is an integer.

    Args:
        n (int): The number variable from the URL.

    Returns:
        str: The formatted message "<n> is a number" if n is an integer, else 404 Not Found.
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000 when the script is executed
    app.run(host='0.0.0.0', port=5000)
