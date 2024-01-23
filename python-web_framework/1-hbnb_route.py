"""
1-hbnb_route.py
~~~~~~~~~~~~~~~~~~~~~
A simple Flask web application with two routes.

Routes:
- /: Display "Hello HBNB!"
- /hbnb: Display "HBNB"

Usage:
python3 1-hbnb_route.py
"""

from flask import Flask

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

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000 when the script is executed
    app.run(host='0.0.0.0', port=5000)
