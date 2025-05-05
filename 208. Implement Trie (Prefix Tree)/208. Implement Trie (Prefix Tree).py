class Trie(object):

    def __init__(self):
        self.vocab = {}
        self.bool = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        ptr = self
        for char in word:
            if char not in ptr.vocab:
                ptr.vocab[char] = Trie()
            ptr = ptr.vocab[char]
        ptr.bool = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        found = False
        ptr = self
        for char in word:
            if ptr and char in ptr.vocab:
                ptr = ptr.vocab[char]
            else:
                return False
        if ptr.bool:
            found=True
        return found


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ptr = self
        for char in prefix:
            if ptr and char in ptr.vocab:
                ptr = ptr.vocab[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)