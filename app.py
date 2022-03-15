from webob import Request, Response

from study_wsgi.api import API

app = API()


@app.route("/home")
def home(request: Request, response: Response):
    response.text = "Hello from home page!"


@app.route("/about")
def about(request: Request, response: Response):
    response.text = "Hello from about page!"


@app.route("/hello/{name:l}")
def hello(request: Request, response: Response, name):
    response.text = f"Hello, {name}!" 