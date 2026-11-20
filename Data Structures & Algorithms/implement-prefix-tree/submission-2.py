class TrieNode:
    def __init__(self, c:str) -> None:
        self.c = c
        self.child: dict[str, TrieNode] = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        parent = self.root
        for c in word:
            if c in parent.child:
                parent = parent.child[c]
            else:
                parent.child[c] = TrieNode(c)
                parent = parent.child[c]
        parent.child["END"] = TrieNode("")

    def search(self, word: str) -> bool:
        parent = self.root
        for c in word:
            if c in parent.child:
                parent = parent.child[c]
            else:
                return False
        if "END" in parent.child:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for c in prefix:
            if c in parent.child:
                parent = parent.child[c]
            else:
                return False
        return True
        
        