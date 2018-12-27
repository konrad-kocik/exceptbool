from contextlib import contextmanager

from exceptbool.bool_wrapper import BoolWrapper


@contextmanager
def except_converter(exc=Exception, to=False):
    result = BoolWrapper(not to)
    try:
        yield result
    except exc:
        result.value = bool(to)
