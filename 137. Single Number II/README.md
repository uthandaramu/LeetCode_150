### 137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

Input: nums = [2,2,3,2]  
Output: 3

**Example 2:**

Input: nums = [0,1,0,1,0,1,99]  
Output: 99

**Constraints:**

1 <= nums.length <= 3 * 104  
-231 <= nums[i] <= 231 - 1  
Each element in nums appears exactly three times except for one element which appears once.

### Brute Force Approach

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        out = None
        for i in range(1, size, 3):
            if nums[i-1] != nums[i]:
                out = nums[i-1]
                break
        if out is None:
            out = nums[-1]
        return out   
```

### With Bit Manipulation 

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        ans = 0
        for bit_place in range(0, 32):
            count = 0
            for element in nums:
                if (element & (1 << bit_place)):
                    count += 1
            if count % 3 == 1:
                ans = ans | (1 << bit_place)
                
        # Handle negative numbers (simulate 32-bit signed int)
        if ans >= 2**31:
            ans -= 2**32

        return ans
```

### Bucket approach (Bit Manipulation)

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        # element goes to ones if it is not in twos
        # element goes to twos if it is in ones
        # element goes to threes(no need) if it is in twos
        # Basically I need two operations, one is to add and other is to remove

        for element in nums:
            ones = (ones ^ element) & (~twos)
            twos = (twos ^ element) & (~ones)

        return ones
```