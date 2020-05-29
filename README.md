# FlaskVersion

## install
```python
pip install itay-bardugo-flask-version -U
```

## Brief
FlaskVersion is a package that helps handle endpoints versions.

## What it solves
assume we have the route
/api/`<version>`/output/endpoint_a

which returns "Hello" to the client.

with Flask it equals to
```python
@app.route("/api/<verrsion>/output/endpoint_a")
def endpoint_a():
    return "Hello"
```

as we can see, `<version>` is a variable which describes our route version.
it can be
`1.0`, `1.1`, `1.2` etc...

what if our server serves clients that ask for this route
in version `1.0`, but we want to add an extra feature to this route, that belongs to version `1.1` only (without changing `1.0`)

we can define a new route for this problem:
```python
@app.route("/api/<verrsion>/output/endoint_b")
def endpoint_a():
    return "Hello new feature!"
```
but we don't want to add new routes for each new feature.

it will be hard to maintain our endpoints and can be a little bit confusing.

this is what `FlaskVersion` was built for!

`FlaskVersion` manages your endpoints by linking each method to one or more version in a few simple steps!
  - Easy to use
  - Easy to maintain

## How to use
All you need to do is:
1. make a new app
```python
    # routes.py
    from flask import Flask
    app = Flask(__name__)
```


2 . make a new callback that returns the version of the current incoming request
```python
    # routes.py
    @app.url_value_preprocessor
    def url_process(endpoint, values):
        if values:
            g.version = values.pop("version", "1.0")
    
    def get_version():
        return g.version
```

3 . make a new instance of FlaskVersion, with your app instance and your version handler callback  
```python
    # routes.py
    from flask_version import FlaskVersion
    flask_version = FlaskVersion(app, url_process)
```

4 . tell to `FlaskVersion` to apply versions on specific route

```python
# routes.py
from flask_version.utils import dispatch

@app.route("/endpoint_a")
@dispatch
def endpoint_a():
    # this is the latest version of the function.
    return "current version!"
```
5 . set the older versions
```python
# versions/endpoint_a.py (important: its called endoint_a.py becuase we used @dispatch on endpoint_a() function
# please note: the structure is
# {route directory}/versions/{function_name}.py
from flask_version.utils import support_version


@support_version("1.0")
def version_a():
    return "i am an endpoint for version 1.0"


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
|   +-- routes.py
|   +-- versions
|       +-- endpoint_a.py

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
