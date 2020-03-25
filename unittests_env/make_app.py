from flask import Flask
from flask_version import FlaskVersion

_app = None


def make_app():
    global _app
    _app = Flask(__name__) if _app is None else _app
    return _app


def make_manager(app=None, get_version=None):
    return FlaskVersion(app, get_version)


from flask import g


def get_version():
    return g.version


app = make_app()
manager = make_manager(app, get_version)


@app.url_value_preprocessor
def dependencies(endpoint, values):
    if values:
        g.version = values.pop("version", "1.0")


# load routes for testing
from . import endpoints
