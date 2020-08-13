from src.callable import Callable


def test_callable():
    callable = Callable()
    assert callable() == 'hi world'
