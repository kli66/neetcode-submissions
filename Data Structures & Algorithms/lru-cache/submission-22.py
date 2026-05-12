from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    key: int = -1
    value: int = -1
    # left backwards, right forwards
    left: Node | None = None
    right: Node | None = None


class DoubleLinkedList:
    def __init__(self):
        self.size: int = 0
        self.head: Node = Node()
        self.tail: Node = Node()

        self.head.right = self.tail
        self.tail.left = self.head

    @property
    def LRU(self) -> Node | None:
        if self.head.right.right is None:
            return None
        else:
            return self.head.right

    def remove(self, node: Node) -> None:
        node.left.right = node.right
        node.right.left = node.left
        self.size -= 1
        return

    def insert_right(self, node: Node) -> Node:
        prev_MRU = self.tail.left
        node.left = prev_MRU
        node.right = self.tail
        prev_MRU.right = node
        self.tail.left = node
        self.size += 1
        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.node_map: dict[int, Node] = {}
        self.node_order_list: DoubleLinkedList = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        else:
            target_node = self.node_map.get(key)
            self.node_order_list.remove(target_node)
            updated_node = self.node_order_list.insert_right(target_node)
            self.node_map[key] = updated_node
            return updated_node.value

    def put(self, key: int, value: int) -> None:

        # adding a brand new node, need to pop
        if key not in self.node_map:
            if self.capacity == self.node_order_list.size:
                curr_LRU = self.node_order_list.LRU
                self.node_order_list.remove(curr_LRU)
                self.node_map.pop(curr_LRU.key)
        else:
            self.node_order_list.remove(self.node_map.get(key))
            self.node_map.pop(key)

        # construct brand new node, insert to right
        new_node = self.node_order_list.insert_right(Node(key, value))
        self.node_map[key] = new_node
        return
