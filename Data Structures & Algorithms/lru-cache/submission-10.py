"""
Pre-allocated Parallel Arrays (Zero-Allocation Structure) courtesy of Gemini:

Instead of creating individual Node objects, we pre-allocate fixed-size lists (arrays) for the keys, values, and pointers. 
We then use integer indices instead of object references.

Why is this radically faster?
1. Zero Instantiation: The self.keys = [0] * size logic runs exactly once during __init__. When the cache runs, it only updates integers inside an existing list. It never calls __new__ or __init__ for a Node ever again.
2. Zero Garbage Collection: When an item is evicted, we don't delete an object. We just take its integer index and push it back onto self.free_indices so it can be overwritten later. The garbage collector never has to step in.
3. Memory Locality: Python lists are arrays of pointers under the hood. Reading contiguous indices in a pre-allocated list is often more CPU-cache friendly than chasing randomly scattered Node objects across your RAM.
4. No Function Call Overhead for Pointers: Because we aren't using @property decorators or traversing dot notation (node.prev.next), Python resolves the array lookups (self.next[idx]) significantly faster.
"""



class LRUCache:

    def __init__(self, capacity: int):  
        self.capacity = capacity
        self.cache: dict[int, int] = {}  # Maps key -> array index
        
        # Total size includes capacity + 2 dummy nodes (index 0=Left, index 1=Right)
        size = capacity + 2
        
        # Pre-allocate arrays (No more object creation during runtime!)
        self.keys = [0] * size
        self.values = [0] * size
        self.prev = [0] * size
        self.next = [0] * size
        
        # Initialize dummy nodes
        self.HEAD = 0
        self.TAIL = 1
        self.next[self.HEAD] = self.TAIL
        self.prev[self.TAIL] = self.HEAD
        
        # Keep track of available indices
        # Indices 2 to capacity+1 are free to use
        self.free_indices = list(range(2, size))

    def _remove_node(self, idx: int) -> None:
        """Unlink an index from the list."""
        p = self.prev[idx]
        n = self.next[idx]
        self.next[p] = n
        self.prev[n] = p

    def _insert_mru(self, idx: int) -> None:
        """Insert an index right before the TAIL."""
        p = self.prev[self.TAIL]
        
        self.prev[idx] = p
        self.next[idx] = self.TAIL
        
        self.next[p] = idx
        self.prev[self.TAIL] = idx

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        idx = self.cache[key]
        self._remove_node(idx)
        self._insert_mru(idx)
        return self.values[idx]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            idx = self.cache[key]
            self.values[idx] = value
            self._remove_node(idx)
            self._insert_mru(idx)
            return

        # If cache is full, evict LRU (which is next to HEAD)
        if not self.free_indices:
            lru_idx = self.next[self.HEAD]
            self._remove_node(lru_idx)
            del self.cache[self.keys[lru_idx]]
            self.free_indices.append(lru_idx) # Reclaim the index
            
        # Get a free index and populate it
        new_idx = self.free_indices.pop()
        self.keys[new_idx] = key
        self.values[new_idx] = value
        self.cache[key] = new_idx
        self._insert_mru(new_idx)