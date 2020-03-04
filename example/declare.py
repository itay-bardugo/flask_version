from flask_version import dispatch


@dispatch
def main(a, b):
    return "i am newest! {} {}".format(a, b)
