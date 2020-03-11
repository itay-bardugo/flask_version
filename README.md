# FlaskVersion

## install
```python
pip install itay-bardugo-flask-version -U
```

## Brief
FlaskVersion is a package that helps handle endpoints versions.

## What it solves
assume we have the route
/api/`<version>`/output/print

which returns "Hello" to the client.

with Flask it equals to
```python
@app.route("/api/<verrsion>/output/print")
def print():
    return "Hello"
```

as we can see, `<version>` is a variable which describes our route version.
it can be
`1.0`, `1.1`, `1.2` etc...

what if our server serves clients that ask for this route
in version `1.0`, but, we want to add an extra feature to this route, which will be visibled only in version `1.1`

we can define a new route for this problem:
```python
@app.route("/api/<verrsion>/output/print_new")
def print():
    return "Hello new feature!"
```
but we dont want to add new routes for each new feature.

it will be hard to maintain our endpoints and can be a little bit confusing.

this is what `FlaskVersion` was built for!

`FlaskVersion` manages your endpoints by linking each method to one or more version in a few simple steps!
  - Easy to use
  - Easy to maintain

## How to use
All you need to do is:

1 . define a callable which returns the current request version before each request

```python
#  main_routes.py
from flask_version import register_version_getter

# set g.version to use it in our app
@app.url_value_preprocessor
def dependencies(endpoint, values):
    if values:
        g.version = values.pop("version", "1.2")


# init data before request
@app.before_request
def before_each_request():
    # register our version detector into flask_version component
    @register_version_getter
    def version_detector():
        return g.version # i.g 1.2 (the newest version)
```

2 . tell to `FlaskVersion` to apply versions on specific route

```python
# ouput_routes.py
from flask_version import dispatch
@app.route("/api/<verrsion>/output/print")
@dispatch # the dispatch decorator tells to FlaskVersion that this method supports older versions
def print():
    # this is the most updated method(latest version).
    #the old versions will be defined in other place
    return "Hello new feature!"
```
3 . set the older versions
```python
#versions/print.py (important: its called print.py becuase we used @dispatch on print() function
# please note: the structrue is
# {specific_routes_folder}/versions/{function_name}.py
from flask_version import apply_version

# this decorator tells to FlaskVersion to apply old() on version "1.0" and "1.1"
@apply_version("1.0")
@apply_version("1.1")
def old():
    return "i am the old version of this route"

```
Thats it, `FlaskVersion` does the job for you and it will route to your
correct endpoint according to the version input

# Structure
basically, it does not matter how you structed your project.
you just have to make sure to follow this structure and `FlaskVersion` will work correctly.
The main idea is to create a new `versions` folder (with an \__init__.py) at the same path where you defined
```python
@app.route("/route/to/some/action")
@dispatch
def action():
    pass
```
and then, create a file inside `versions` with the same name (in this case `action.py`), the inside this file, just create your old versions of your endpoint

## Example to Structre A:
```
+-- project
|   +-- main_routes.py
|   +-- output_routes.py
|   +-- versions
|       +-- print.py

```
## Example to Structre B:
```
+-- project
|   +-- main_routes.py
|   +-- blueprints
|       +-- output
|           +-- routes.py
|           +-- versions
|               +-- {function_name that @dispatch was applyed on it}.py
|       +-- user
|           +-- routes.py
|           +-- versions
|               +-- {function_name that @dispatch was applyed on it}.py

```


License
----

MIT
