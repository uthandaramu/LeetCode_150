### 74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.  
The first integer of each row is greater than the last integer of the previous row.  
Given an integer target, return true if target is in matrix or false otherwise.  

You must write a solution in O(log(m * n)) time complexity.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" width="300">

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  
Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" width="300">

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13  
Output: false

**Constraints:**

* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 100
* -104 <= matrix[i][j], target <= 104

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        visited = set()

        row = len(matrix)
        col = len(matrix[0])

        start, end = 0, (row*col) - 1

        while start <= end:

            mid = (start + end) // 2
            i = mid // col
            j = mid % col

            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
```