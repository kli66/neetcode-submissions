from dataclasses import dataclass

@dataclass(slots=True)
class Node:
    key: int
    value: int
    prev_: Node | None = None
    next_: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        # maps from key to Node
        self.cache: dict[int, Node] = {}
        self.curr_size: int = 0

        # left's right is LRU
        self.left: Node = Node(-1,-1)
        self.right: Node = Node(-2,-2)

        self.left.next_ = self.right
        self.right.prev_ = self.left


    def get(self, key: int) -> int:
        result = self.cache.get(key, None)

        # need to move to front
        if result != None:
            self.pluck(result)
            self.insert_right(result)
            return result.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.pluck(self.cache.get(key))
        
        new_node = Node(key, value)
        self.insert_right(new_node)

        if self.curr_size > self.capacity:
            self.pluck(self.left.next_)

        return 


    def pluck(self, node: Node) -> None:
        if node.prev_ is None or node.next_ is None:
            return 
        else:
            node.prev_.next_ = node.next_
            node.next_.prev_ = node.prev_ 
            self.curr_size -= 1
            del self.cache[node.key]
    
    def insert_right(self, node: Node) -> None:
        old_MRU = self.right.prev_
        old_MRU.next_ = node
        self.right.prev_ = node
        node.next_ = self.right
        node.prev_ = old_MRU
        
        self.curr_size += 1
        self.cache[node.key] = node
        return
        


