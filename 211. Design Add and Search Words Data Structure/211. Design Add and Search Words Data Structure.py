class Trie:
    def __init__(self):
        self.child = {}
        self.isEnd = False

    def insert(self, word):
        ptr = self
        for char in word:
            if char not in ptr.child:
                ptr.child[char] = Trie()

            ptr = ptr.child[char]
        ptr.isEnd = True


class WordDictionary(object):

    def __init__(self):
        self.head = Trie()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.head.insert(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(index, node):
            ptr = node
            for i in range(index, len(word)):
                char = word[i]
                if char != ".":
                    if char not in ptr.child:
                        return False
                    ptr = ptr.child[char]
                else:
                    for letter_node in ptr.child.values():
                        if dfs(i + 1, letter_node):
                            return True
                    return False

            return True if ptr.isEnd else False

        return dfs(0, self.head)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)