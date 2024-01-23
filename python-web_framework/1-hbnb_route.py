from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/").
    
    Displays a simple greeting message "Hello HBNB!" when the root URL is accessed.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

# Define a route for the "/hbnb" URL with strict_slashes=False
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
