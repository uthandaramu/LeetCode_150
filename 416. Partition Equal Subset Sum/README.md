### 416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

**Example 1:**

Input: nums = [1,5,11,5]  
Output: true  
Explanation: The array can be partitioned as [1, 5, 5] and [11].  

**Example 2:**

Input: nums = [1,2,3,5]  
Output: false  
Explanation: The array cannot be partitioned into equal sum subsets.  

**Constraints:**

1 <= nums.length <= 200  
1 <= nums[i] <= 100  

### With Recursion(optimized)

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        half_sum = total_sum / 2

        dp_arr = [[False for _ in range(half_sum + 1)] for _ in range(size)]

        def rec_partition(idx, target):
            if target == 0:
                return True
            if idx == 0:
                return nums[idx] == target
            if dp_arr[idx][target] == -1:
                not_take = rec_partition(idx-1, target)
                take = False
                if nums[idx] <= target:
                    take = rec_partition(idx-1, target - nums[idx])
                dp_arr[idx][target] = take or not_take
            return dp_arr[idx][target]

        return (rec_partition(size-1, half_sum))
```

### With Dynamic Programming(Tabulation)

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        half_sum = total_sum/2

        dp_arr = [[False for _ in range(half_sum+1)] for _ in range(size)]

        for i in range(size):
            dp_arr[i][0] = True

        if nums[0] <= half_sum:
            dp_arr[0][nums[0]] = True
        
        for idx in range(1, size):
            for target in range(1, half_sum+1):
                not_take = dp_arr[idx-1][target]
                take = False
                if nums[idx] <= target:
                    take = dp_arr[idx-1][target - nums[idx]]
                dp_arr[idx][target] = take or not_take
        return dp_arr[size-1][half_sum]  
```

### Dynamic Programing (Space Optimized)

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        half_sum = total_sum/2

        prev_arr = [False for _ in range(half_sum+1)]

        prev_arr[0] = True

        if nums[0] <= half_sum:
            prev_arr[nums[0]] = True
        
        for idx in range(1, size):
            cur_arr = [False for _ in range(half_sum+1)]
            cur_arr[0] = True
            for target in range(1, half_sum+1):
                not_take = prev_arr[target]
                take = False
                if nums[idx] <= target:
                    take = prev_arr[target - nums[idx]]
                cur_arr[target] = take or not_take
            prev_arr = cur_arr
        return prev_arr[half_sum]
            
```