from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a route and corresponding function
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run()
