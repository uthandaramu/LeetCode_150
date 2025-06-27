### 79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" width="200">

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  
Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" width="200">

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"  
Output: true

**Example 3:**

<img src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" width="200">

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"  
Output: false

**Constraints:**

m == board.length  
n = board[i].length  
1 <= m, n <= 6  
1 <= word.length <= 15  
board and word consists of only lowercase and uppercase English letters.  
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        visited_path = set()

        def rec_search(r, c, letter_idx):
    
            if letter_idx == len(word):
                return True
            if r >= row or c >= col or r < 0 or c < 0 or word[letter_idx] != board[r][c] or (r, c) in visited_path:
                return False

            visited_path.add((r, c))
            result = (rec_search(r, c+1, letter_idx+1) or 
                        rec_search(r, c-1, letter_idx+1) or 
                        rec_search(r-1, c, letter_idx+1) or 
                        rec_search(r+1, c, letter_idx+1))
            visited_path.remove((r, c))
            return result
        
        for i in range(row):
            for j in range(col):
                if rec_search(i, j, 0):
                    return True
        return False
```