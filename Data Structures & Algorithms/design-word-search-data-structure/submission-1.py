class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.word = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(node, index):
            if index == n:
                return node.word
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            elif char in node.children:
                return dfs(node.children[char], index + 1)
            return False

        return dfs(self.root, 0)