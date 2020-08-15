from pytest import mark

from src.math import Math


sum_params = (
    (Math(value=1), Math(value=2), Math(value=3)),
    (Math(value=1), 2, Math(value=3)),
)


@mark.parametrize('value0, value1, result', sum_params)
def test_sum(value0, value1, result):
    assert value0 + value1 == result


def test_sub():
    math0 = Math(value=3)
    math1 = Math(value=1)
    assert math0 - math1 == Math(value=2)


def test_mul():
    math0 = Math(value=3)
    math1 = Math(value=2)
    assert math0 * math1 == Math(value=6)
