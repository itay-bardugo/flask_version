from unittests_env import make_app
from flask import g
from flask_version.utils import dispatch

app = make_app.make_app()


@app.route("/<version>")
@dispatch
def endpoint_a():
    return "current version!"


@app.route("/<version>/sayHello")
@dispatch
def endpoint_b():
    return "Hello version {}".format(g.version)
