from functools import wraps
import inspect
import importlib.util
from .meta import Singleton
from .exceptions import StopMatchException, VersionIdentifierException
from .interfaces import VersionConfig


class Dispatcher(metaclass=Singleton):
    _namespaces = {}

    def __init__(self):
        self._request_version = None

    def _has_match(self, ns):
        version_config = self._get_namespace(ns)
        spec = importlib.util.spec_from_file_location(version_config.get_version_filename(), version_config.get_versioned_module())
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except StopMatchException:
            ...

        return version_config.has_target()

    def version(self, version):
        version = str(version)

        def wrapper(fn):
            frame = inspect.stack()[1]
            version_config = self._get_namespace(frame.filename)
            if version_config.version == version:
                version_config.add_target(fn)
                raise StopMatchException()
            return fn

        return wrapper

    def _get_namespace(self, ns) -> 'VersionConfig':
        return self._namespaces.get(ns, None)

    def _add_namespace(self, version_config: 'VersionConfig'):
        key = version_config.get_key()
        self._namespaces[key] = version_config
        return key

    def dispatch(self, source_fn):
        frame = inspect.stack()[1]

        @wraps(source_fn)
        def versioned(*args, **kwargs):
            if not callable(self._request_version):
                raise VersionIdentifierException(
                    "please use register_version_getter decorator "
                    "so the process will know the version that was called")

            ns = self._add_namespace(VersionConfig(frame, source_fn, self._request_version))

            if self._has_match(ns):
                return self._get_namespace(ns).apply_target(*args, **kwargs)
            return source_fn(*args, **kwargs)

        return versioned

    def register_version_getter(self, fn):
        self._request_version = fn

        def wrapper():
            return fn()

        return wrapper
