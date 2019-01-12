class ConvertedExcept:
    def __init__(self, value):
        self._value = bool(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)
