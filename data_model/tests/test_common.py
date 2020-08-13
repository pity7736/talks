from src.common import Common


def test_common():
    """this is not a real test
    It's just for see print statements.
    Try exchange del and print statement positions
    """
    obj = Common()
    del obj
    print('hi')


def test_repr():
    obj = Common()
    assert repr(obj) == '<Common>'


def test_str():
    obj = Common()
    assert str(obj) == 'Common'
