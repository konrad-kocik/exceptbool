class BoolWrapper:
    def __init__(self, bool_to_wrap):
        self._wrapped_bool = None
        self.wrap(bool_to_wrap)

    def __repr__(self):
        return repr(self._wrapped_bool)

    def __bool__(self):
        return self._wrapped_bool

    def wrap(self, bool_to_wrap):
        self._wrapped_bool = bool(bool_to_wrap)
