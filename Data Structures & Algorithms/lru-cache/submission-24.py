# using built in OrderedDict

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()
        

    def get(self, key: int) -> int:
        if not key in self.d:
            return -1
        else:
            self.d.move_to_end(key)
            return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)
        return 