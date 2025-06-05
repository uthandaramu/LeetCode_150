### 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

Input: nums = [2,2,1]

Output: 1

**Example 2:**

Input: nums = [4,1,2,1,2]

Output: 4

**Example 3:**

Input: nums = [1]

Output: 1

**Constraints:**

1 <= nums.length <= 3 * 104  
-3 * 104 <= nums[i] <= 3 * 104  
Each element in the array appears twice except for one element which appears only once.

### With Brute Force

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        out = None
        for i in range(1, size, 2):
            if nums[i-1] != nums[i]:
                out = nums[i-1]
                break
        if out is None:
            out = nums[-1]
        return out
```

### With Bit manipulation

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
            if count % 2 == 1:
                ans = ans | (1 << bit_place)
        
        if ans >= 2**31:
            ans -= 2 ** 32
        return ans
```

### With Bit manipulation (Optimized approach)

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bucket Approach
        # Element will go to ones if it is not in twos
        # Element will go to twos(ignorable) if it is in ones
        ones = 0
        for element in nums:
            ones = (ones ^ element) & (~0)  
                
        return ones
```