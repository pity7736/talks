from pytest import raises

from src.dict_slot import NormalClass, SlotClass


def test_dict():
    obj = NormalClass(1, 'hi', 'world')

    assert obj.__dict__ == {'a': 1, 'b': 'hi', 'c': 'world'}
    assert vars(obj) == {'a': 1, 'b': 'hi', 'c': 'world'}
    obj.d = 'new attribute'
    assert vars(obj) == {'a': 1, 'b': 'hi', 'c': 'world', 'd': 'new attribute'}


def test_slot():
    obj = SlotClass(1, 'hi', 'world')

    with raises(AttributeError):
        print(obj.__dict__)

    with raises(AttributeError):
        obj.d = 'new attribute'

