
class Container:

    def __init__(self):
        self._data = {}
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        values = list(self._data.values())
        if self._i < len(self._data):
            result = values[self._i]
            self._i += 1
            return result
        raise StopIteration

    def __getitem__(self, item):
        try:
            return self._data[item]
        except KeyError:
            raise AttributeError(f'{self} has not attribute {item}')

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in (*self._data.keys(), *self._data.values())

