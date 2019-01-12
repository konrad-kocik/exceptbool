from contextlib import contextmanager

from exceptbool.converted_except import ConvertedExcept


@contextmanager
def except_converter(*, exc=Exception, to=False):
    result = ConvertedExcept(not to)
    try:
        yield result
    except exc:
        result.value = to
