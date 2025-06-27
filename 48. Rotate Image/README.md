### 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" width="350">

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]  
Output: [[7,4,1],[8,5,2],[9,6,3]]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" width="350">

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]  
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

**Constraints:**

* n == matrix.length == matrix[i].length
* 1 <= n <= 20
* -1000 <= matrix[i][j] <= 1000

### Without any extra space (not preferable)

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        n = 3
        [0][0] -> [0][2]
        [0][1] -> [1][2]
        [0][2] -> [2][2]
        [1][0] -> [0][1]
        [1][1] -> [1][1]
        [r][c] -> [c][(n-1)-r]
        """

        n = len(matrix)

        out = [[0 for _ in range(n)] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                out[c][(n-1)-r] = matrix[r][c]
        
        print(out)
```

### With No extra space (preferable)

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        orgMatrix ---> Transpose ---> reverse elements in the row ----> output
        """

        n = len(matrix)

        #Transpose
        # for transpose diagnal elements([0][0], [1][1], ..) will be in same place
        # we need to swap only upper triangle
        """
        n = 4
        [0][1] - > [1][0]  |  [1][2] - > [2][1]  |  [2][3] - > [3][2]
        [0][2] - > [2][0]  |  [1][3] - > [3][1]  |
        [0][3] - > [3][0]  |                     |
                
        [0 to (n-2)][(r+1) to (n-1)] - > swap
        """

        for r in range(n-1):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        #Reverse the elements in each row:
        for r in range(n):
            matrix[r].reverse()
```