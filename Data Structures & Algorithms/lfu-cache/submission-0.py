from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    key: int
    value: int
    left: Node | None = None
    right: Node | None = None
    freq: int = 1


class DoublyLinkedList:
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

    @property
    def is_empty(self) -> bool:
        return self.head.right == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        # maps from frequency to left node in each DLL, which points to the LRU in that freq
        self.freq_cache: dict[int, DoublyLinkedList] = {}
        # maps from key to Node
        self.node_cache: dict[int, Node] = {}
        self.capacity: int = capacity
        self.min_freq: int = 0

    def get(self, key: int) -> int:
        if key in self.node_cache:
            curr_node = self.node_cache.get(key)
            # remove the node from the old row
            self.pluck(curr_node)
            # insert a node to the new frequency row
            curr_node.freq += 1
            self.insert(curr_node)
            return curr_node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_cache:
            curr_node = self.node_cache.get(key)
            self.pluck(curr_node)
            # insert a node to the new frequency row
            curr_node.value = value
            curr_node.freq += 1
            self.insert(curr_node)

        else:
            new_node = Node(key, value)
            self.node_cache[key] = new_node
            # insert the new node to the corresponding frequency row (1)
            self.insert(new_node)
            self.min_freq = 1

    def evict(self) -> None:
        """
        always drop the LRU element in the LFU collection DLL
        """
        if not self.node_cache:
            return None
        elif self.min_freq not in self.freq_cache:
            raise KeyError
        else:
            # find the target node and pluck
            target_node = self.freq_cache.get(self.min_freq).head.right
            self.pluck(target_node)
            return 

    def insert(self, node: Node) -> None:
        # insert the node to the freq row indicated by its field
        if not self.freq_cache.get(node.freq):
            self.freq_cache[node.freq] = DoublyLinkedList()

        self.freq_cache[node.freq].insert_right(node)

        # if over sized, need to evict
        self.node_cache[node.key] = node
        if len(self.node_cache) > self.capacity:
            self.evict()

        # can we devise a unified solution for updating min_freq?
        # situation where we need to alter:
        # 1. inserting a brand new node - always set to 1
        # 2. inserting an existing node to a new row, we are advancing its counter
        #   so if its original DLL is empty, we advance to the new one? no - could skip a row
        #   safer way is to check if current min_freq is empty - we then update to the new one
        if node.freq == 1 or self.freq_cache.get(self.min_freq) is None:
            self.min_freq = node.freq


    def pluck(self, node: Node) -> None:
        # remove the node from the old row
        curr_dll = self.freq_cache.get(node.freq)
        if not curr_dll:
            raise ValueError
        else:
            node.left.right = node.right
            node.right.left = node.left
            del self.node_cache[node.key]

            if curr_dll.is_empty:
                del self.freq_cache[node.freq]
        
