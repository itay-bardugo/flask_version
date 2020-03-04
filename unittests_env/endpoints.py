from flask_version import dispatch


@dispatch
def endpoint_a():
    return "current version!"
