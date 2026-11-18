class ListNode:
    def __init__(self, k=-1, v=-1, prv=None, nxt=None):
        self.k = k
        self.v= v
        self.prv = prv
        self.nxt = nxt




class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.LRU = ListNode()
        self.MRU = ListNode()
        self.LRU.nxt = self.MRU
        self.MRU.prv = self.LRU
        self.d = dict()
    
    def _insert(self, node:ListNode):
        node.prv, node.nxt = self.MRU.prv, self.MRU
        self.MRU.prv.nxt = node
        self.MRU.prv = node
        return
    
    def _delete(self, node: ListNode):
        node.prv.nxt, node.nxt.prv = node.nxt, node.prv
        return

    def get(self, key: int) -> int:
        if not key in self.d:
            return -1
        else:
            node = self.d.get(key)
            self._delete(node)
            self._insert(node)
            return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            target = self.d[key]
            self._delete(target)     
            target.v = value
        else:
            target = ListNode(key, value)
            if len(self.d) == self.cap:
                evictee = self.LRU.nxt
                self._delete(evictee)
                self.d.pop(evictee.k)

        self._insert(target)
        self.d[key] = target
        
