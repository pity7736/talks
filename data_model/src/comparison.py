from typing import Union


class Comparison:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other: Union['Comparison', int]):
        if isinstance(other, Comparison):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __le__(self, other: Union['Comparison', int]):
        if isinstance(other, Comparison):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        return NotImplemented
