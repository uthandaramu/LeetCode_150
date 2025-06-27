### 212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" width="200">

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]  
Output: ["eat","oath"]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg">

Input: board = [["a","b"],["c","d"]], words = ["abcb"]  
Output: []

**Constraints:**

m == board.length  
n == board[i].length  
1 <= m, n <= 12  
board[i][j] is a lowercase English letter.  
1 <= words.length <= 3 * 104  
1 <= words[i].length <= 10  
words[i] consists of lowercase English letters.  
All the strings of words are unique.  

### Without Trie (Cause TLE Error)

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        col = len(board[0])

        visited_path = set()

        def rec_find(r_id, c_id, letter_id, cur_word):
            if letter_id == len(cur_word):
                return True
            if r_id >= row or c_id >= col or r_id < 0 or c_id < 0 or board[r_id][c_id] != cur_word[letter_id] or ((r_id, c_id) in visited_path):
                return False
            visited_path.add((r_id, c_id))
            result = (rec_find(r_id, c_id-1, letter_id+1, cur_word) or
                        rec_find(r_id, c_id+1, letter_id+1, cur_word) or
                        rec_find(r_id+1, c_id, letter_id+1, cur_word) or
                        rec_find(r_id-1, c_id, letter_id+1, cur_word))
            visited_path.remove((r_id, c_id))
            return result
        
        out_arr = []
        for word in words:
            found = False
            for i in range(row):
                for j in range(col):
                    if rec_find(i, j, 0, word):
                        out_arr.append(word)
                        found = True
                        break
                if found:
                    break
        
        return (out_arr) 
```

### With Trie (Optimized)

```python
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

        #store the found words in set to avoid duplicates
        result_word = set()
        #store the visited path along the way to avoid infinite recursion as we move in four directional
        visited_path = set()

        def rec_search(r_id, c_id, trie_node, word):

            #row and col out of bound case, board letter not in our trie
            if r_id < 0 or c_id < 0 or r_id == row or c_id == col or (r_id, c_id) in visited_path or board[r_id][c_id] not in trie_node.children:
                return
            
            #store the visited index for time being
            visited_path.add((r_id, c_id))

            #continuing furthen in the trie node to check the next character search
            trie_node = trie_node.children[board[r_id][c_id]]
            word += board[r_id][c_id]

            if trie_node.is_Word:
                result_word.add(word)
            
            #Move in four direction
            rec_search(r_id, c_id+1, trie_node, word)
            rec_search(r_id, c_id-1, trie_node, word)
            rec_search(r_id+1, c_id, trie_node, word)
            rec_search(r_id-1, c_id, trie_node, word)

            #remove the visited index as backtracing purpose and as we may visit it again for different word search
            visited_path.remove((r_id, c_id))

        for i in range(row):
            for j in range(col):
                rec_search(i, j, root, "")

        return list(result_word)       
```