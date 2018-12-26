from exceptbool import except_converter


def test_except_converter_returns_false_when_exception_raised():
    with except_converter() as converted_exception:
        raise Exception()

    assert converted_exception.value is False


def test_except_converter_returns_true_when_exception_not_raised():
    with except_converter() as converted_exception:
        pass

    assert converted_exception.value is True


def test_except_converter_returns_true_before_exception_is_raised():
    with except_converter() as converted_exception:
        assert converted_exception.value is True
        raise Exception()


def test_except_converter_changes_returned_value_to_false_after_exception_is_raised():
    with except_converter() as converted_exception:
        assert converted_exception.value is True
        raise Exception()

    assert converted_exception.value is False


def test_except_converter_str_representation_of_converted_exception_is_false_when_exception_raised():
    with except_converter() as converted_exception:
        raise Exception()

    assert str(converted_exception) == 'False'


def test_except_converter_str_representation_of_converted_exception_is_true_when_exception_not_raised():
    with except_converter() as converted_exception:
        pass

    assert str(converted_exception) == 'True'
