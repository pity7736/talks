from typing import Dict, Any


class AttrAccess:

    __slots__ = ('_data',)

    def __init__(self, data: Dict[str, Any]):
        self._data = data

    def __getattribute__(self, item):
        if item == 'attr':
            return 'hi'
        return super().__getattribute__(item)

    def __getattr__(self, item):
        try:
            return self._data[item]
        except KeyError:
            raise AttributeError(f'{self} has not attribute {item}')

    def __setattr__(self, key, value):
        if key == '_data':
            super().__setattr__(key, value)
            return
        self._data[key] = value

    def __delattr__(self, item):
        del self._data[item]
