from dataclasses import dataclass
 

@dataclass(slots=True)
class Node:
    """
    data storage
    """

    key: int
    value: int
    left: Node | None = None
    right: Node | None = None
    freq: int = 1


class DoublyLinkedList:
    """
    pointer manipulation
    """

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.right, self.tail.left = self.tail, self.head

    def insert_right(self, node: Node) -> None:
        old_mru = self.tail.left
        node.left, node.right = old_mru, self.tail
        old_mru.right = node
        self.tail.left = node
        return

    @staticmethod
    def pluck(node: Node) -> None:
        node.left.right = node.right
        node.right.left = node.left
        node.left = node.right = None

    @property
    def is_empty(self) -> bool:
        return self.head.right == self.tail

    @property
    def lru_node(self) -> Node:
        """Provides O(1) read access to the eviction candidate."""
        return self.head.right


class LFUCache:
    """
    orchestration
    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.min_freq: int = 0
        # maps from frequency to left node in each DLL, which points to the LRU in that freq
        self.freq_cache: dict[int, DoublyLinkedList] = {}
        # maps from key to Node
        self.node_cache: dict[int, Node] = {}

    # region internal (handles cache updates)
    def _insert(self, node: Node) -> None:
        if node.freq not in self.freq_cache:
            self.freq_cache[node.freq] = DoublyLinkedList()
        self.freq_cache[node.freq].insert_right(node)
        self.node_cache[node.key] = node

    def _pluck(self, node):
        del self.node_cache[node.key]
        dll = self.freq_cache.get(node.freq)
        dll.pluck(node)
        if dll.is_empty:
            del self.freq_cache[node.freq]

    def _update(self, node: Node) -> None:
        self._pluck(node)

        # If we just emptied the min_freq list, the global min_freq must increment
        if self.min_freq == node.freq and node.freq not in self.freq_cache:
            self.min_freq += 1

        node.freq += 1
        self._insert(node)

    # endregion

    # region exposed
    def get(self, key: int) -> int:
        if key not in self.node_cache:
            return -1

        node = self.node_cache[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.node_cache:
            node = self.node_cache[key]
            node.value = value
            self._update(node)
            return
        
        # new node, check if we need to clear space first
        if len(self.node_cache) == self.capacity:
            target_dll = self.freq_cache.get(self.min_freq)
            victim = target_dll.lru_node
            self._pluck(victim)

        new_node = Node(key, value)
        self._insert(new_node)
        self.min_freq = 1


    # endregion
