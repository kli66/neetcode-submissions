from dataclasses import dataclass
from collections import OrderedDict

@dataclass(slots=True)
class Node:
    key: int
    value: int


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        # maps from key to Node
        self.cache: OrderedDict[int, Node] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True)
        return self.cache.get(key).value

    def put(self, key: int, value: int) -> None:
        self.cache[key] = Node(key, value)
        self.cache.move_to_end(key, last=True)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        return 




