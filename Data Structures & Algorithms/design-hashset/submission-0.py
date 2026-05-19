# since we are doing int key and val, storing a singular list where idx is the key and the associated value is value is also possible.
# but this would require sparse list? could consider pre-allocate and trim. okay given the input size? still wasteful.

# what other do we have? we can start the hashing stuff by our own, modulo maps nice with int keys?
# since # of calls is also limited, can do modulo 10000? or possibly smaller

# so, given a key, do hash by key % modulo_const -> hashed key
# store the value as a member of a list inside said key.
# org key also need to be stored for cache collision

_MODULO_DIVISOR = 100


class MyHashSet:
    def __init__(self):
        self._storage: list[list[int]] = [[]] * _MODULO_DIVISOR

    def add(self, key: int) -> None:
        hashed_key = self._hash(key)
        if not self._storage[hashed_key]:
            self._storage[hashed_key] = [key]
        else:
            for curr_key in self._storage[hashed_key]:
                if curr_key == key:
                    break
            else:
                self._storage[hashed_key].append(key)
            return

    def remove(self, key: int) -> None:
        hashed_key = self._hash(key)
        # easy path, hashed not in storage
        if not self._storage[hashed_key]:
            return None
        else:
            for idx, val in enumerate(self._storage[hashed_key]):
                if val == key:
                    break
            else:
                # nothing found
                return None

            # break, found something
            # would it possible for us to update inplace here instead of assigning again?
            new_bin = self._storage[hashed_key]
            new_bin.pop(idx)
            self._storage[hashed_key] = new_bin
        return

    def contains(self, key: int) -> bool:
        hashed_key = self._hash(key)
        # easy path, hashed not in storage
        if not self._storage[hashed_key]:
            return False
        else:
            for curr_key in self._storage[hashed_key]:
                if curr_key == key:
                    return True
            return False

    @staticmethod
    def _hash(key: int) -> int:
        return key % _MODULO_DIVISOR


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
