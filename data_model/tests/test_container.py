from pytest import fixture, raises

from src.container import Container


@fixture
def container():
    return Container()


def test_getitem_and_setitem(container):
    container['a'] = 'hi world'

    assert container['a']


def test_length(container):
    assert len(container) == 0
    container['a'] = 1
    container['b'] = 2
    container['c'] = 3
    assert len(container) == 3


def test_delitem(container):
    container['a'] = 1
    assert container['a'] == 1
    del container['a']
    with raises(AttributeError):
        container['a']


def test_contains(container):
    container['a'] = 1

    assert ('a' in container) is True
    assert (1 in container) is True


def test_iter(container):
    container['a'] = 1
    container['b'] = 2
    container['c'] = 3
    for i in container:
        print(i)


def test_async_iter(container):
    container['a'] = 1
    container['b'] = 2
    container['c'] = 3
    async for i in container:
        print(i)
