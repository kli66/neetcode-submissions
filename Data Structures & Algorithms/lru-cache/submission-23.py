class Node:
    def __init__(self, k=-1, v=-1, prv=None, nxt=None):
        self.k = k
        self.v = v
        self.prv = prv
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = dict()
        # ptrs to start and end only - not actual nodes
        self.LRU = Node()
        self.MRU = Node()
        self.LRU.nxt = self.MRU
        self.MRU.prv = self.LRU

    def _remove(self, node: Node) -> None:
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv

    def _insert(self, node: Node) -> None:
        prev = self.MRU.prv
        prev.nxt = node
        node.prv = prev
        node.nxt = self.MRU
        self.MRU.prv = node

    def put(self, k: int, v: int) -> None:
        if not k in self.d:
            target = Node(k,v)
        else:
            target = self.d.get(k)
            self._remove(target)
            target.v = v

        self._insert(target)
        self.d[k] = target
        if len(self.d) > self.cap:
            evictee = self.LRU.nxt
            self._remove(evictee)
            self.d.pop(evictee.k)

    
    def get(self, k: int) -> int:
        if not k in self.d:
            return -1
        else:
            target = self.d.get(k)
            self._remove(target)
            self._insert(target)
            return target.v


