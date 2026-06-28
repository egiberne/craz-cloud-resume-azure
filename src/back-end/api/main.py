# Create the environment variable to run the app with waitress : python -m venv env 
# Activate the virtual environment : .env/venv/bin/activate
# Install the dependencies : pip install waitress 
# Run the  WSGI server : waitress-serve --listen=127.0.0.1:8080 main:invoke_app


import json

def invoke_app(environ, set_header):
    """Function to handle incoming requests and return a response."""
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    set_header(status, headers)
    body_response = b"Hello world!\n"
    return [body_response]

