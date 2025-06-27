### 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" width="250">

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]  
Output: [1,2,3,6,9,8,7,4,5]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" width="250">

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  
Output: [1,2,3,4,8,12,11,10,9,5,6,7] 

**Constraints:**

* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 10
* -100 <= matrix[i][j] <= 100

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])

        #Right -> Bottom -> Left -> Up

        left = 0
        top = 0
        right = col-1
        bottom = row-1

        out = []

        while left <= right and top <= bottom:
            #Printing right
            for i in range(left, right+1):
                out.append(matrix[top][i])
            
            top += 1

            #Printing Bottom
            for i in range(top, bottom+1):
                out.append(matrix[i][right])

            right -= 1
            if top <= bottom:
                #Printing Left
                for i in range(right, left-1, -1):
                    out.append(matrix[bottom][i])
                
                bottom -= 1

            if right >= left:
                #Printing Up
                for i in range(bottom, top-1, -1):
                    out.append(matrix[i][left])
                
                left += 1

        return (out)
```