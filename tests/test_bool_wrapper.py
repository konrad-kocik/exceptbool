from pytest import fixture, mark

from exceptbool.bool_wrapper import BoolWrapper


@fixture
def wrapped_true():
    return BoolWrapper(bool_to_wrap=True)


@fixture
def wrapped_false():
    return BoolWrapper(bool_to_wrap=False)


@mark.parametrize('expected_bool', [True, False])
def test_init_sets_correct_wrapped_bool(expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=expected_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


@mark.parametrize('not_a_bool, expected_bool', [("a", True), ("", False)])
def test_init_sets_correct_wrapped_bool_when_wrapping_not_a_bool(not_a_bool, expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=not_a_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


@mark.parametrize('expected_bool', [True, False])
def test_wrap_changes_wrapped_bool_to_correct_value(expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=not expected_bool)
    bool_wrapper.wrap(bool_to_wrap=expected_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


@mark.parametrize('not_a_bool, expected_bool', [("a", True), ("", False)])
def test_wrap_changes_wrapped_bool_to_correct_value_when_wrapping_not_a_bool(not_a_bool, expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=not expected_bool)
    bool_wrapper.wrap(bool_to_wrap=not_a_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


def test_bool_representation_of_wrapped_true_is_true(wrapped_true):
    assert wrapped_true
    assert bool(wrapped_true) is True


def test_bool_representation_of_wrapped_false_is_false(wrapped_false):
    assert not wrapped_false
    assert bool(wrapped_false) is False


def test_bool_wrapper_str_representation_of_wrapped_true_is_same_as_str_representation_of_true(wrapped_true):
    assert str(wrapped_true) == str(True)
    assert repr(wrapped_true) == repr(True)


def test_bool_wrapper_str_representation_of_wrapped_false_is_same_as_str_representation_of_false(wrapped_false):
    assert str(wrapped_false) == str(False)
    assert repr(wrapped_false) == repr(False)
