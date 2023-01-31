import logging


class ValidationError(Exception):
    pass


def exception(exc=ValidationError, msg='', log=True):
    def exception_(f):
        def wrapper(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
                return ret
            except Exception:
                if log: logging.exception(msg)
                raise exc(msg)
            
        wrapper.__qualname__ = f.__qualname__
        return wrapper

    return exception_
