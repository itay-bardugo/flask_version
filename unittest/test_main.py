from unittest import TestCase
from flask_version import register_version
from unittests_env import endpoints


class TestBase(TestCase):
    def test_current_version(self):
        @register_version
        def get_version():
            return "1.2"
        self.assertEqual(endpoints.endpoint_a(), "current version!", "expected output: current version!")

    def test_old_vresion(self):
        @register_version
        def get_version():
            return "1.0"
        self.assertEqual(endpoints.endpoint_a(), "i am an endpoint for version 1.0", "expected output: i am an endpoint for version 1.0")
