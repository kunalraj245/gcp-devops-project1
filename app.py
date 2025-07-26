from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Simple Flask application"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# app.py
# Ensure that Flask is installed in your environment
# You can install it using pip:
# pip install Flask
# To run the application, use the command:
# python app.py
# This will start the Flask development server on port 5000, accessible from all network interfaces
# Note: This is a development server and should not be used in production.
# For production, consider using a WSGI server like Gunicorn or uWSGI.