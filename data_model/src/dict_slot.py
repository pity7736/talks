
class NormalClass:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class SlotClass:

    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
