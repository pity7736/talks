from pytest import raises, fixture

from src.attr_access import AttrAccess


@fixture
def obj():
    return AttrAccess(data={'a': 1, 'b': 'hi world'})


def test_getattribute(obj):
    assert obj.attr == 'hi'
    with raises(AttributeError):
        print(obj.hi)


def test_getattr(obj):
    assert obj.a == 1
    assert obj.b == 'hi world'


def test_setattr(obj):
    obj.c = 'new attribute'
    assert obj.c == 'new attribute'


def test_delattr(obj):
    del obj.a
    with raises(AttributeError):
        print(obj.a)

