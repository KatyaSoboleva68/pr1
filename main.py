from wsgiref.simple_server import make_server

from typing import Callable

HOST = "localhost"
PORT = 8080
SCHEMA = "http"


class ReverseWare:

    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(environ, start_response)
        return [data[::-1] for data in wrapped_app_response]


def application(environ, start_response):
    response_body = "\n".join([f"{key}:{value}" for key, value in sorted(environ.items())])

    status = "200 OK"

    response_headers = [("Content-type", "text/plain")]

    start_response(status, response_headers)

    return [response_body.encode("utf-8")]


server = make_server("localhost", 8080, app=ReverseWare(application))
print(f"Serving on {SCHEMA}://{HOST}:{PORT}")
server.serve_forever() 