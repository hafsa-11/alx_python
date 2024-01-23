from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/").
    Displays "Hello HBNB!" when the root URL is accessed.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

# Run the application on 0.0.0.0:5000 when the script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
