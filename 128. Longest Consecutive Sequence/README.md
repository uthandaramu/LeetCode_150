### 128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example 1:**

**Input:** nums = [100,4,200,1,3,2]  
**Output:** 4  
**Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.  

**Example 2:**

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]  
**Output:** 9

**Example 3:**

**Input:** nums = [1,0,1,2]  
**Output:** 3

**Constraints:**

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109

### Better (not preferable)

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        size = len(nums)
        curLong = 0
        maxLong = 0
        lastMin = -10 ** 9

        for i in range(size):
            if nums[i]-1 == lastMin:
                curLong += 1
            elif nums[i] != lastMin:
                curLong = 1

            lastMin = nums[i]
            maxLong = max(maxLong, curLong)
        
        return (maxLong)
```

### Optimal Approach (preferred)

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set(nums)
        maxCount = 0

        for val in elements:
            curCount = 1
            if val-1 not in elements:
                while val+1 in elements:
                    curCount += 1
                    val = val+1

            maxCount = max(curCount, maxCount)
        
        return (maxCount)
```