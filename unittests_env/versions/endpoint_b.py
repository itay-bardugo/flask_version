from unittests_env import make_app
from flask import g
from flask_version.utils import support_version


@support_version("1.0")
def version_a():
    return "Hello version {}".format(g.version)
