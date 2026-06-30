# Create the environment variable to run the app with wsgi server : python -m venv env 
# Activate the virtual environment : env/script/activate
# Install the dependencies : pip install <wsgi-server-package>
# Run the  WSGI server : <wsgi-server-command>  <python-file>:<wsgi_app-function>
# For instance, to run the app with waitress, you can use the following command:  waitress-serve --listen=127.0.0.1:8080 main:wsgi_app


import json


def wsgi_app(environ, start_response):
    """Function to handle incoming requests and return a response."""
    method = environ["REQUEST_METHOD"]
    path_info = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]
    headers = [('Content-type', 'text/plain')]

    if path_info == "/wsgi/v1/visits":
        status = "200 OK"
        if method == "GET":
            body_response = b"Thank you for visiting!\n"

        elif method == "POST":
            content_length=int(environ["CONTENT_LENGTH"])
            body_receive =environ["wsgi.input"].read(content_length)
            data = json.loads(body_receive)
            user_id = data.get("userId","")
            body_response =f"User ID  {user_id}!\n".encode('utf-8')

        else:
            status ="405 Method Not Allowed"
            body_response = b"Method Not Allowed!\n"

    else:
        status = "404 Not Found"
        body_response = b"Not Found!\n"

    
    start_response(status, headers)
    return [body_response]

