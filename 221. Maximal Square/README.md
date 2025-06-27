### 221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" width="300">

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  
Output: 4

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" width="200">

Input: matrix = [["0","1"],["1","0"]]  
Output: 1

**Example 3:**

Input: matrix = [["0"]]  
Output: 0

**Constraints:**

m == matrix.length  
n == matrix[i].length  
1 <= m, n <= 300  
matrix[i][j] is '0' or '1'.  

### Own flow

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        col = len(matrix[0])
        row = len(matrix)
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]

        maxi = 0

        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp_arr[i][j] = int(matrix[i][j])
                if j == 0:
                    dp_arr[i][j] = int(matrix[i][j])
                if (i - 1) >= 0 and (j - 1) >= 0:
                    if int(matrix[i][j]) == 1 and dp_arr[i][j - 1] > 0 and dp_arr[i - 1][j] > 0 and dp_arr[i - 1][
                        j - 1] > 0:
                        dp_arr[i][j] = min(dp_arr[i][j - 1], dp_arr[i - 1][j], dp_arr[i - 1][j - 1]) + 1
                    else:
                        dp_arr[i][j] = int(matrix[i][j])
                maxi = max(maxi, dp_arr[i][j])

        return (maxi * maxi)
```

### Optimized

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]
        maxi = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp_arr[i][j] = 1
                    else:
                        dp_arr[i][j] = min(
                            dp_arr[i-1][j],        # top
                            dp_arr[i][j-1],        # left
                            dp_arr[i-1][j-1]       # top-left
                        ) + 1
                    maxi = max(maxi, dp_arr[i][j])

        return maxi * maxi
```

