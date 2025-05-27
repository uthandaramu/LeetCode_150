### 120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

**Example 1:**

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]  
Output: 11  
Explanation: The triangle looks like:  
   2  
  3 4  
 6 5 7  
4 1 8 3  
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

**Example 2:**

Input: triangle = [[-10]]  
Output: -10

**Constraints:**

1 <= triangle.length <= 200  
triangle[0].length == 1  
triangle[i].length == triangle[i - 1].length + 1  
-104 <= triangle[i][j] <= 104  

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

### With Recursion

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])

        def recur_tri(i, j):
            if i == row - 1:
                return triangle[i][j]
            down = triangle[i][j] + recur_tri(i + 1, j)
            diagnol = triangle[i][j] + recur_tri(i + 1, j + 1)
            return min(down, diagnol)

        return (recur_tri(0, 0))
```

### With Dynamic Programming

```python
import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        dp_arr = [[sys.maxint for _ in range(col)] for _ in range(row)]
        def recur_tri(i, j):
            if i == row-1:
                return triangle[i][j]
            if dp_arr[i][j] == sys.maxint: 
                down = triangle[i][j] + recur_tri(i+1, j)
                diagnol = triangle[i][j] + recur_tri(i+1, j+1)
                dp_arr[i][j] = min(down, diagnol)
            return dp_arr[i][j]
        
        return (recur_tri(0, 0))
```

### With Dynamic Programming (Tabulation)

```python
import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        dp_arr = [[sys.maxint for _ in range(col)] for _ in range(row)]
        dp_arr[-1] = triangle[-1]
        for i in range(row-2, -1, -1):
            for j in range(i, -1, -1):
                up = triangle[i][j] + dp_arr[i+1][j]
                diagnol = triangle[i][j] + dp_arr[i+1][j+1]
                dp_arr[i][j] = min(up, diagnol)
        
        return (dp_arr[0][0])
```
### With Dynamic Programming(Space Optimization)

```python
import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        prev_arr = triangle[-1]
        for i in range(row-2, -1, -1):
            cur_arr=[0 for _ in range(i+1)]
            for j in range(i, -1, -1):
                up = triangle[i][j] + prev_arr[j]
                diagnol = triangle[i][j] + prev_arr[j+1]
                cur_arr[j] = min(up, diagnol)
            prev_arr = cur_arr
        return (prev_arr[0])
```