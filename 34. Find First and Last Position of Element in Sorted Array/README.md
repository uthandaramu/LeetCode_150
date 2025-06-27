### 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**

Input: nums = [5,7,7,8,8,10], target = 8  
Output: [3,4]

**Example 2:**

Input: nums = [5,7,7,8,8,10], target = 6  
Output: [-1,-1]

**Example 3:**

Input: nums = [], target = 0  
Output: [-1,-1]
 

**Constraints:**

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums is a non-decreasing array.
* -109 <= target <= 109

### Brute Force Approach

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        first = last = -1

        for i in range(size):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first, last]
```

### Using lower bound and upper bound approach

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = lower_b = len(nums)
        first = last = -1

        #lower bound
        start = 0
        end = size - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                lower_b = mid
                end = mid - 1
            else:
                start = mid + 1
            
        if lower_b == size or nums[lower_b] != target:
            return [first, last]
        
        #upper bound
        start = 0
        end = size - 1
        upper_b = size

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                upper_b = mid
                end = mid -1
            else:
                start = mid + 1
        
        return [lower_b, upper_b-1]
```

### Optimal Approach (using plain binary search)

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Plain binary search approach

        size = len(nums)

        first = last = -1

        start, end = 0, size-1
        
        #Identify first occurence
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        
        if first == -1:
            return [first, last]

        #Identify last occurece
        start , end = first, size-1
        
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                start = mid + 1
                last = mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        
        return [first, last]
```