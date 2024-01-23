"""
2-c_route.py
~~~~~~~~~~~~~~~~
A Flask web application with multiple routes.

Routes:
- /: Display "Hello HBNB!"
- /hbnb: Display "HBNB"
- /c/<text>: Display "C " followed by the value of the text variable
             (replace underscore _ symbols with a space)

Usage:
python3 2-c_route.py
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

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000 when the script is executed
    app.run(host='0.0.0.0', port=5000)
