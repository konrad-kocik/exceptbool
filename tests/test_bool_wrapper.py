from exceptbool.bool_wrapper import BoolWrapper


def test_bool_wrapper_str_representation_of_wrapped_false_is_str_false():
    wrapped_false = BoolWrapper(False)

    assert str(wrapped_false) == 'False'


def test_bool_wrapper_str_representation_of_wrapped_true_is_str_true():
    wrapped_true = BoolWrapper(True)

    assert str(wrapped_true) == 'True'
