### 73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" width="400">

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]  
Output: [[1,0,1],[0,0,0],[1,0,1]]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" width="400">

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]  

**Constraints:**

m == matrix.length  
n == matrix[0].length  
1 <= m, n <= 200  
-231 <= matrix[i][j] <= 231 - 1  

**Follow up:**

A straightforward solution using O(mn) space is probably a bad idea.  
A simple improvement uses O(m + n) space, but still not the best solution.  
Could you devise a constant space solution?

### Brute Force (Direct approach)

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        row_arr = [0 for _ in range(row)]
        col_arr = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_arr[i] = 1
                    col_arr[j] = 1
        
        for i in range(row):
            for j in range(col):
                if (row_arr[i] == 1 or col_arr[j] == 1):
                    matrix[i][j] = 0
```

### Space Optimized solution (Optional)

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        col0 = 1

        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(row):
                matrix[i][0] = 0
```