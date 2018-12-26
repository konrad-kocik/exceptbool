from contextlib import contextmanager


class ConvertedException:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


@contextmanager
def except_converter(exc=Exception, to=False):
    result = ConvertedException(not to)
    try:
        yield result
    except exc:
        result.value = to
