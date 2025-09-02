import flask
import functions_framework

@functions_framework.http
def hello(request: flask.Request) -> flask.typing.ResponseReturnValue:
    return "Hello world! Again X3 testing no gitmoji branch"
