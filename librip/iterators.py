# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self._items = items
        self._ignore = 'ignore_case' in kwargs.keys()
        self._buf = []
        self._index = -1
        self._max_index = len(items)
        print(items)
    def __next__(self):
        while (1):
            self._index += 1
            if self._index >= self._max_index:
                raise StopIteration
            b = self._items[self._index]
            if b not in self._buf:
                self._buf.append(b)
                return b
    def __iter__(self):
        return self