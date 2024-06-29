class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for l in word:
            if l not in root.children:
                root.children[l] = Node()
            root = root.children[l]
        root.is_word = True        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx==len(word):
                return node.is_word

            res = False
            l = word[idx]
            if l=='.':
                for child in node.children.values():
                    res = res or dfs(child, idx+1)
                    if res:
                        break

            elif l in node.children:
                res = res or dfs(node.children[l], idx+1)
            return res

        root = self.root
        return dfs(root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)