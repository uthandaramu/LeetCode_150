### 494. Target Sum

You are given an integer array nums and an integer target.  

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.  

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".  
Return the number of different expressions that you can build, which evaluates to target.  

**Example 1:**

Input: nums = [1,1,1,1,1], target = 3  
Output: 5  
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.  
-1 + 1 + 1 + 1 + 1 = 3  
+1 - 1 + 1 + 1 + 1 = 3  
+1 + 1 - 1 + 1 + 1 = 3  
+1 + 1 + 1 - 1 + 1 = 3  
+1 + 1 + 1 + 1 - 1 = 3  

**Example 2:**

Input: nums = [1], target = 1  
Output: 1  

**Constraints:**

1 <= nums.length <= 20  
0 <= nums[i] <= 1000  
0 <= sum(nums[i]) <= 1000  
-1000 <= target <= 1000  

### With Recursion

```python
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        size = len(nums)

        def rec_sum(idx, target):
            if idx == 0:
                if target == 0 and nums[idx] == 0:
                    return 2
                if target == 0 or nums[idx] == target:
                    return 1
                return 0
            
            not_pick = rec_sum(idx-1, target)
            pick = 0 
            if nums[idx] <= target:
                pick = rec_sum(idx-1, target-nums[idx])
            return (pick + not_pick)
        
        if (total_sum - target) >= 0 and (total_sum - target)%2 == 0:
            return rec_sum(size-1, (total_sum - target)/2)
        else:
            return 0
```

### With Dynamic Programing

```python
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        size = len(nums)

        dp_arr = [[-1 for _ in range(((total_sum - target)/2)+1)] for _ in range(size)]

        def rec_sum(idx, target):
            if idx == 0:
                if target == 0 and nums[idx] == 0:
                    return 2
                if target == 0 or nums[idx] == target:
                    return 1
                return 0
            if dp_arr[idx][target] == -1:
                not_pick = rec_sum(idx-1, target)
                pick = 0 
                if nums[idx] <= target:
                    pick = rec_sum(idx-1, target-nums[idx])
                dp_arr[idx][target] = (pick + not_pick)
            return dp_arr[idx][target]
        
        if (total_sum - target) >= 0 and (total_sum - target)%2 == 0:
            return rec_sum(size-1, (total_sum - target)/2)
        else:
            return 0
```

### With Dynamic Programing(Tabulation)

```python
class Solution(object):
    def helper(self, index, target):
        if self.nums[0] == 0:
            self.dp_arr[0][0] = 2
        else:
            self.dp_arr[0][0] = 1
        
        if self.nums[0] != 0 and self.nums[0] <= target:
            self.dp_arr[0][self.nums[0]] = 1
        
        for idx in range(1, index+1):
            for tar in range(target+1):
                not_take = self.dp_arr[idx-1][tar]
                take = 0
                if self.nums[idx] <= tar:
                    take = self.dp_arr[idx-1][tar-self.nums[idx]]
                self.dp_arr[idx][tar] = take + not_take
        return self.dp_arr[index][target]

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.target = target
        self.total_sum = sum(nums)
        self.size = len(nums)

        self.dp_arr = [[0 for _ in range(((self.total_sum - self.target)//2)+1)] for _ in range(self.size)]

        if (self.total_sum - self.target) >= 0 and (self.total_sum - self.target)%2 == 0:
            return self.helper(self.size-1, (self.total_sum - self.target)//2)
        else:
            return 0
```

