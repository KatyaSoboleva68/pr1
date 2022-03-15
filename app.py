from webob import Request, Response

from study_wsgi.api import API
from study_wsgi.base.base_view import BaseView

app = API()


@app.route("/home")
def home(request: Request, response: Response):
    response.text = "Hello from home page!"

@app.route("/players")
class PlayerView:
    def get(self, request: Request, response: Response, **kwargs):
        pass

@app.route("/about")
def about(request: Request, response: Response):
    response.text = "Hello from about page!"


@app.route("/hello/{name:l}")
def hello(request: Request, response: Response, name):
    response.text = f"Hello, {name}!" 
@app.route("/home")
def home(request: Request, response: Response):
    response.text = "Hello from home page!"