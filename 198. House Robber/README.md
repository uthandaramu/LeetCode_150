### 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

**Example 1:**

Input: nums = [1,2,3,1]  
Output: 4  
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).  
Total amount you can rob = 1 + 3 = 4.  

**Example 2:**

Input: nums = [2,7,9,3,1]  
Output: 12  
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).  
Total amount you can rob = 2 + 9 + 1 = 12.

**Constraints:**

1 <= nums.length <= 100  
0 <= nums[i] <= 400  

### With Dynamic Programming (Memory Optimized)

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp_arr = [-1]*(size)
        def dp_rob(cur_idx):
            if cur_idx >= size:
                return 0
            if dp_arr[cur_idx] == -1:
                pick = nums[cur_idx] + dp_rob(cur_idx+2)
                not_pick = dp_rob(cur_idx+1)
                dp_arr[cur_idx] = max(pick, not_pick)
            return dp_arr[cur_idx]
        return dp_rob(0)
```

### With Dynamic Programming (Space Optimized)

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1, size):
            take = nums[i] + prev2
            non_take = 0 + prev
            cur_max = max(take, non_take)
            prev2 = prev
            prev = cur_max
        return prev
```

[2,7,9,3,1]