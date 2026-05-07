
from typing import Any
from dataclasses import dataclass

@dataclass
class Node:
    key: int = 0
    value: int = 0
    prev_: Node | None = None
    next_: Node | None = None


class DoubleLinkedList:

    def __init__(self) -> None:

        # LRU
        self.left = Node()
        # MRU
        self.right = Node()
        self.left.next_ = self.right
        self.right.prev_ = self.left
    
    def insert(self, node: Node) -> None:
        """
        always insert to MRU
        """
        old_mru = self.right.prev_
        
        # Wire up the new node
        node.prev_ = old_mru
        node.next_ = self.right
        
        # Wire up the surroundings
        old_mru.next_ = node
        self.right.prev_ = node
    
    def pop(self) -> Node | None:
        """
        always removes the LRU, unlink it from the current list
        """
        if self.left.next_ == self.right:
            return None # List is empty
            
        lru_node = self.left.next_
        self.remove(lru_node)
        return lru_node
    
    def remove(self, node: Node) -> None:
        """
        removes a fixed Node
        """
        prev_node = node.prev_
        next_node = node.next_
        
        # Bypass the node being removed
        prev_node.next_ = next_node
        next_node.prev_ = prev_node



class LRUCache:

    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._cache: dict[int, Node] = {}
        self._linked_list: DoubleLinkedList = DoubleLinkedList()

    def get(self, key: int) -> int:
        """
        get a value from the cache, do not insert 
        """
        if key in self._cache:
            node = self._cache[key]
            # Move to MRU by removing and re-inserting
            self._linked_list.remove(node)
            self._linked_list.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        insert/update a value to the cache
        """
        if key in self._cache:
            # UPDATE existing node
            node = self._cache[key]
            self._linked_list.remove(node)
            node.value = value # Update the payload
            self._linked_list.insert(node)
        else:
            # CREATE new node
            new_node = Node(key, value)
            self._cache[key] = new_node
            self._linked_list.insert(new_node)

            # EVICT if capacity is exceeded
            if len(self._cache) > self._capacity:
                popped_lru = self._linked_list.pop()
                if popped_lru:
                    del self._cache[popped_lru.key] # Delete the CORRECT key
