import flask
import functions_framework


@functions_framework.http
def hello_world(request: flask.Request):
    return {"hello": "world"}
