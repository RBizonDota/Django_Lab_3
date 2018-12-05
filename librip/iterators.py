# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self._items = items
        self.ignore = 0
        if 'ignore_case' in kwargs.keys():
            if (kwargs['ignore_case']==1):
                self.ignore = 1
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
            if self.ignore:
                if str(b).lower() not in self._buf:
                    self._buf.append(str(b))
                    return b
            else:
                if str(b) not in self._buf:
                    self._buf.append(str(b))
                    return b
    def __iter__(self):
        return self