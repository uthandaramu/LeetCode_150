### 149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" width="250">

Input: points = [[1,1],[2,2],[3,3]]  
Output: 3

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" width="250">

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  
Output: 4
 

**Constraints:**

* 1 <= points.length <= 300
* points[i].length == 2
* -104 <= xi, yi <= 104
* All the points are unique.

**Note:** It can also be solved with normal hash (**Only Key difference:** Auto Handling on missing keys)

```python
from fractions import Fraction
from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        size = len(points)

        max_points = 1

        for i in range(size):
            hash_slope = defaultdict(int)
            point1 = points[i]

            for j in range(i+1, size):
                point2 = points[j]
                
                if point1[0] == point2[0]:
                    slope = "inf"
                else:
                    slope = Fraction((point2[1] - point1[1]), (point2[0] - point1[0]))
                
                hash_slope[slope] += 1

                max_points = max(max_points, hash_slope[slope] + 1)
            
        return max_points
```