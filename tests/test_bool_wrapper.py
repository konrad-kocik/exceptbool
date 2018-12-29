from pytest import mark

from exceptbool.bool_wrapper import BoolWrapper


@mark.parametrize('expected_bool', [True, False])
def test_init_sets_correct_wrapped_bool(expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=expected_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


@mark.parametrize('expected_bool', [True, False])
def test_wrap_changes_wrapped_bool_to_correct_value(expected_bool):
    bool_wrapper = BoolWrapper(bool_to_wrap=not expected_bool)
    bool_wrapper.wrap(bool_to_wrap=expected_bool)

    assert bool_wrapper._wrapped_bool is expected_bool


def test_bool_representation_of_wrapped_false_is_false():
    assert not BoolWrapper(bool_to_wrap=False)


def test_bool_representation_of_wrapped_true_is_true():
    assert BoolWrapper(bool_to_wrap=True)


def test_bool_wrapper_str_representation_of_wrapped_false_is_str_false():
    wrapped_false = BoolWrapper(False)

    assert str(wrapped_false) == 'False'


def test_bool_wrapper_str_representation_of_wrapped_true_is_str_true():
    wrapped_true = BoolWrapper(True)

    assert str(wrapped_true) == 'True'
