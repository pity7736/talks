from pytest import raises

from src.comparison import Comparison


def test_less_than():
    obj0 = Comparison(value=1)
    obj1 = Comparison(value=2)

    assert obj0 < obj1
    assert obj0 < 2
    with raises(TypeError):
        obj0 < 'hi'


def test_less_than_or_equal():
    obj0 = Comparison(value=1)
    obj1 = Comparison(value=1)

    assert obj0 <= obj1
    assert obj0 <= 1
    with raises(TypeError):
        obj0 <= 'hi'
