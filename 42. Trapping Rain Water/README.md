### 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example 1:**

<img src = "https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" width="350">

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]  
**Output:** 6  
**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

**Example 2:**

**Input:** height = [4,2,0,3,2,5]   
**Output:** 9
 

**Constraints:**

* n == height.length
* 1 <= n <= 2 * 104
* 0 <= height[i] <= 105

### With Extra Space

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        prefixMax = [0] * size
        suffixMax = [0] * size

        prefixMax[0] = height[0]
        suffixMax[-1] = height[-1]

        #Identifying prefix max
        for i in range(1, size):
            prefixMax[i] = max(prefixMax[i-1], height[i])
        
        #Identifying suffix max
        for i in range(size-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], height[i])
        
        result = 0
        for i in range(size):
            if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
                result += min(prefixMax[i], suffixMax[i]) - height[i]
        
        return result
```

### Without extra space

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        leftMax = rightMax = left = result = 0
        right = size-1

        while left < right:

            if height[left] <= height[right]:
                if height[left] < leftMax:
                    result += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1

            else:
                if height[right] < rightMax:
                    result += rightMax - height[right]
                else:    
                    rightMax = height[right]
                right -= 1

        return result
```