from functools import wraps

from .loader import Loader


def cli_loader(start_desc, end_desc):
    """Decorate on functions you want loader on"""

    def decorater(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            loader = Loader(start_desc, end_desc)
            loader.start_loader_simple()
            func(*args, **kwargs)
            loader.stop_loader()

        return wrapper
    return decorater
