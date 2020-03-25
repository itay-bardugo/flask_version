from unittest import TestCase
from unittests_env import make_app

app = make_app.make_app()


def response(uri):
    with app.test_client() as client:
        rv = client.get(uri)
        return rv.data.decode("utf-8")


class TestApp(TestCase):
    def test_simple_current(self):
        self.assertEqual(response("/1.2"), "current version!")

    def test_simple_older(self):
        self.assertEqual(response("/1.0"), "i am an endpoint for version 1.0")

    def test_another_route_current_version(self):
        self.assertEqual(response("/1.2/sayHello"), "Hello version 1.2")

    def test_another_route_older(self):
        self.assertEqual(response("/1.0/sayHello"), "Hello version 1.0")
