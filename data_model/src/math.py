from typing import Union


class Math:

    def __init__(self, value):
        self._value = value

    def __add__(self, other: Union['Math']):
        if isinstance(other, int):
            return Math(value=self._value + other)
        return Math(value=self._value + other._value)

    def __sub__(self, other: Union['Math']):
        return Math(value=self._value - other._value)

    def __eq__(self, other: Union['Math']):
        return self._value == other._value

    def __mul__(self, other):
        return Math(value=self._value * other._value)
