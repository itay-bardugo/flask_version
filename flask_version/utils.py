from flask import current_app
from . import FlaskVersion

_UTILS_FRAME_LEVEL = 2


def dispatch(fn):
    with FlaskVersion().get_app_context():
        return current_app.versions_dispatcher.dispatch(fn, _UTILS_FRAME_LEVEL)


def support_version(version):
    with FlaskVersion().get_app_context():
        return current_app.versions_dispatcher.version(version)
