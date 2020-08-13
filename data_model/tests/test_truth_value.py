from src.truth_value import TrueObject, FalseLenObject, FalseBoolObject, LenBoolObject


def test_true_object():
    assert bool(TrueObject()) is True


def test_false_with_len():
    assert bool(FalseLenObject()) is False


def test_false_with_bool():
    assert bool(FalseBoolObject()) is False


def test_show_priority_between_len_and_bool():
    print(bool(LenBoolObject()))
