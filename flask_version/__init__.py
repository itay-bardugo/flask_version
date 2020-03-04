from .version_dispatcher import Dispatcher

_dispatcher = Dispatcher()
dispatch = _dispatcher.dispatch
apply_version = _dispatcher.version
register_version_getter = _dispatcher.register_version_getter
