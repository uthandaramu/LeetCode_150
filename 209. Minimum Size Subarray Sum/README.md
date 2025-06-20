209. Minimum Size Subarray Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

### Brute Force

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        out = size + 1
        start = ptr = 0
        while ptr < size:
            tar = target
            start = ptr
            cur_length = 0
            while tar > 0 and start < size:
                tar -= nums[start]
                cur_length += 1
                start += 1
            if tar > 0:
                cur_length = size + 1
            out = min(out, cur_length)
            ptr = ptr + 1
        
        return out if out != size + 1 else 0
```
### Optimized Solution

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        out = size + 1
        left = 0
        total = 0
        for right in range(size):
            total += nums[right]
            while total >= target:
                out = min(out, right - left + 1)
                total -= nums[left]
                left += 1

        return out if out != size + 1 else 0
```