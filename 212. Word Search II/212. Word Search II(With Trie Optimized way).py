class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_Word = False

    def add_word(self, word):
        # Create a Trie datastructure
        ptr = self
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.is_Word = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        col = len(board[0])

        root = TrieNode()

        # Insert words in trie
        for word in words:
            root.add_word(word)

        # store the found words in set to avoid duplicates
        result_word = set()
        # store the visited path along the way to avoid infinite recursion as we move in four directional
        visited_path = set()

        def rec_search(r_id, c_id, trie_node, word):

            # row and col out of bound case, board letter not in our trie
            if r_id < 0 or c_id < 0 or r_id == row or c_id == col or (r_id, c_id) in visited_path or board[r_id][
                c_id] not in trie_node.children:
                return

            # store the visited index for time being
            visited_path.add((r_id, c_id))

            # continuing furthen in the trie node to check the next character search
            trie_node = trie_node.children[board[r_id][c_id]]
            word += board[r_id][c_id]

            if trie_node.is_Word:
                result_word.add(word)

            # Move in four direction
            rec_search(r_id, c_id + 1, trie_node, word)
            rec_search(r_id, c_id - 1, trie_node, word)
            rec_search(r_id + 1, c_id, trie_node, word)
            rec_search(r_id - 1, c_id, trie_node, word)

            # remove the visited index as backtracing purpose and as we may visit it again for different word search
            visited_path.remove((r_id, c_id))

        for i in range(row):
            for j in range(col):
                rec_search(i, j, root, "")

        return list(result_word)