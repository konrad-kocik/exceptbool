from pytest import raises

from exceptbool import except_converter


def test_except_converter_converts_to_wrapped_false_when_exception_raised():
    with except_converter() as converted_exception:
        raise Exception()

    assert not converted_exception


def test_except_converter_converts_to_wrapped_true_when_exception_not_raised():
    with except_converter() as converted_exception:
        pass

    assert converted_exception


def test_except_converter_converts_to_wrapped_true_before_exception_raised():
    with except_converter() as converted_exception:
        assert converted_exception
        raise Exception()


def test_except_converter_changes_converted_value_to_wrapped_false_after_exception_raised():
    with except_converter() as converted_exception:
        assert converted_exception
        raise Exception()

    assert not converted_exception


def test_except_converter_converts_to_given_wrapped_bool_when_given_exception_raised():
    with except_converter(exc=ValueError, to=True) as converted_exception:
        raise ValueError()

    assert converted_exception


def test_except_converter_converts_to_given_wrapped_bool_negation_when_given_exception_not_raised():
    with except_converter(exc=TimeoutError, to=True) as converted_exception:
        pass

    assert not converted_exception


def test_except_converter_converts_to_given_wrapped_bool_when_sub_exception_raised():
    with except_converter(exc=Exception, to=True) as converted_exception:
        raise TypeError()

    assert converted_exception


def test_except_converter_does_not_catch_exception_when_exception_different_than_given_exception_raised():
    different_exception = FileNotFoundError

    with raises(different_exception):
        with except_converter(exc=AttributeError):
            raise different_exception()


def test_except_converter_raises_exception_when_given_exception_is_not_an_exception():
    with raises(TypeError) as exc:
        with except_converter(exc=None):
            raise RuntimeError

    assert 'catching classes that do not inherit from BaseException is not allowed' in str(exc)


def test_except_converter_converts_to_wrapped_bool_representation_when_to_is_not_a_bool():
    with except_converter(to="") as converted_exception:
        raise TimeoutError

    assert not converted_exception


def test_except_converter_converts_to_negated_wrapped_bool_representation_when_to_is_not_a_bool():
    with except_converter(to="") as converted_exception:
        pass

    assert converted_exception
