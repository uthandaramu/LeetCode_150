### 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2],[-1,0,1]]  
Explanation:   
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.  
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.  
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.  
The distinct triplets are [-1,0,1] and [-1,-1,2].  
Notice that the order of the output and the order of the triplets does not matter.

**Example 2:**

Input: nums = [0,1,1]  
Output: []  
Explanation: The only possible triplet does not sum up to 0.

**Example 3:**

Input: nums = [0,0,0]  
Output: [[0,0,0]]  
Explanation: The only possible triplet sums up to 0.
 

**Constraints:**

3 <= nums.length <= 3000  
-105 <= nums[i] <= 105

### Better Approach

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        out_set = set()
        for i in range(size):
            temp_dict = {}
            for j in range(i+1, size):
                target = - (nums[i] + nums[j])
                if target in temp_dict:
                    out_set.add(tuple(sorted((nums[i], nums[j], target))))
                else:
                    temp_dict[nums[j]] = 1
        
        return list(out_set)
```

### Optimal Approach

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        nums.sort()
        out_set = set()
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = size-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    out_set.add(tuple((nums[i], nums[j], nums[k])))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            
        return list(out_set)
```