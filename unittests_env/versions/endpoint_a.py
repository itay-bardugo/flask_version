from flask_version import apply_version


@apply_version("1.0")
def version_a():
    return "i am an endpoint for version 1.0"
