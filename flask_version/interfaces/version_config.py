from inspect import FrameInfo
import os


class VersionConfig:
    def __init__(self, frame: FrameInfo, caller_method, version: callable):
        self._frame = frame
        self._caller_method = caller_method
        self._version = version
        self._target = None

    @property
    def version(self):
        return str(self._version())

    def add_target(self, target: callable):
        self._target = target

    def has_target(self):
        return callable(self._target)

    def apply_target(self, *args, **kwargs):
        return self._target(*args, **kwargs)

    def get_versioned_module(self):
        filename = self.get_file_name()
        return filename[:filename.rfind(os.path.sep) + 1] + f"versions{os.path.sep}{self.get_version_filename()}.py"

    def get_version_filename(self):
        return self._caller_method.__name__

    def get_key(self):
        return self.get_versioned_module()

    def get_caller_method_name(self):
        return self._caller_method.__name__

    def get_file_name(self):
        return self._frame.filename
