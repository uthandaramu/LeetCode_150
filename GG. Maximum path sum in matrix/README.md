### Maximum path sum in matrix

You are given a matrix mat[][] of size n x m where each element is a positive integer. Starting from any cell in the first row, you are allowed to move to the next row, but with specific movement constraints. From any cell (r, c) in the current row, you can move to any of the three possible positions :

(r+1, c-1) — move diagonally to the left.  
(r+1, c) — move directly down.  
(r+1, c+1) — move diagonally to the right.  
Find the maximum sum of any path starting from any column in the first row and ending at any column in the last row, following the above movement constraints.  

**Examples :**

Input: mat[][] = [[3, 6, 1], [2, 3, 4], [5, 5, 1]]  
Output: 15  
Explaination: The best path is (0, 1) -> (1, 2) -> (2, 1). It gives the maximum sum as 15.  

Input: mat[][] = [[2, 1, 1], [1, 2, 2]]  
Output: 4  
Explaination: The best path is (0, 0) -> (1, 1). It gives the maximum sum as 4.  

Input: mat[][] = [[25]]  
Output: 25  
Explaination: (0, 0) is the only cell in mat[][], so maximum path sum will be 25.  

**Constraints:**  

1 ≤ mat.size() ≤ 500  
1 ≤ mat[i].size() ≤ 500  
1 ≤ mat[i][j] ≤ 1000  

### With Recursion

```python
class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])
        
        def rec_max(i, j):
            if i < 0 or j < 0 or i > row-1 or j> col-1:
                return 0
            if i == row-1:
                return mat[i][j]
            down = mat[i][j] + rec_max(i+1, j)
            left_diagnol = mat[i][j] + rec_max(i+1, j-1)
            right_diagnol = mat[i][j] + rec_max(i+1, j+1)
            return max(down, left_diagnol, right_diagnol)

        out = 0
        for i in range(col):
            cur = rec_max(0, i)
            out = max(out, cur)
        return out
```

### With Dynamic Programming

```python
class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])
        
        dp_arr = [[-1 for _ in range(col)] for _ in range(row)]
        
        def rec_max(i, j):
            if i < 0 or j < 0 or i > row-1 or j> col-1:
                return 0
            if i == row-1:
                return mat[i][j]
            if dp_arr[i][j] == -1:
                down = mat[i][j] + rec_max(i+1, j)
                left_diagnol = mat[i][j] + rec_max(i+1, j-1)
                right_diagnol = mat[i][j] + rec_max(i+1, j+1)
                dp_arr[i][j] = max(down, left_diagnol, right_diagnol)
            return dp_arr[i][j]
        
        out = 0
        for i in range(col):
            cur = rec_max(0, i)
            out = max(out, cur)
        return out
```

### With Dynamic Programming (Tabulation)


```python
class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])
        
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]
        dp_arr[-1] = mat[-1][:]
        
        def rec_max(i, j):
            for i in range(row-2, -1, -1):
                for j in range(col):
                    up = mat[i][j] + dp_arr[i+1][j]
                    left_diagnol = (mat[i][j] + dp_arr[i+1][j-1]) if (j-1 >= 0 ) else 0
                    right_diagnol = (mat[i][j] + dp_arr[i+1][j+1]) if (j+1 <= col-1) else 0
                    dp_arr[i][j] = max(up, left_diagnol, right_diagnol)
            return max(dp_arr[0])

        out = 0
        for i in range(col):
            cur = rec_max(row-1, i)
            out = max(out, cur)
        return out
```

### With Dynamic Programming(Space optimized)

```python
class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])
        
        def rec_max(i, j):
            prev_arr = [0 for _ in range(col)]
            prev_arr = mat[-1][:]
            for i in range(row-2, -1, -1):
                cur_arr = [0 for _ in range(col)]
                for j in range(col):
                    up = mat[i][j] + prev_arr[j]
                    left_diagnol = (mat[i][j] + prev_arr[j-1]) if (j-1 >= 0 ) else 0
                    right_diagnol = (mat[i][j] + prev_arr[j+1]) if (j+1 <= col-1) else 0
                    cur_arr[j] = max(up, left_diagnol, right_diagnol)
                prev_arr = cur_arr
            return max(prev_arr)

        out = 0
        for i in range(col):
            cur = rec_max(row-1, i)
            out = max(out, cur)
        return out
```