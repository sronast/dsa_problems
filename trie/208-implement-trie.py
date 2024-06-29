class Node:
    def __init__(self, val=''):
        self.val=val
        self.is_word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for l in word:
            if l not in root.children:
                child = Node(l)
                root.children[l] = child
            root = root.children[l]
        root.is_word = True
            

    def search(self, word: str) -> bool:
        root = self.root
        for l in word:
            if l not in root.children:
                return False
            root = root.children[l]
        return root.is_word
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for l in prefix:
            if l not in root.children:
                return False
            root = root.children[l]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)