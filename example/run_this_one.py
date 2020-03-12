from flask_version import register_version
from example.declare import main


@register_version
def version():
    return "1.1"  # change it to "1.0" to invoke the older version


print(main("hi", "there"))
