from flask_version import apply_version


@apply_version("1.0")
def old(a, b):
    return 'i am old... {} {}'.format(a, b)
