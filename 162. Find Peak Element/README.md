### 162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

**Example 1:**

Input: nums = [1,2,3,1]  
Output: 2  
Explanation: 3 is a peak element and your function should return the index number 2.

**Example 2:**

Input: nums = [1,2,1,3,5,6,4]  
Output: 5  
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

**Constraints:**

* 1 <= nums.length <= 1000
* -231 <= nums[i] <= 231 - 1
* nums[i] != nums[i + 1] for all valid i.

### Brute Force Approach

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = peak = 0
        size = len(nums)

        for i in range(size):
            if (i == 0 or nums[i-1] < nums[i]) and (i == size-1 or nums[i] > nums[i+1]):
                return i
```

### Optimized Binary Search Approach

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        #Edge Case for 1 element 
        if size == 1:
            return 0

        #Edge cases for corner elements
        if nums[0] > nums[1]:
            return 0
        
        if nums[size-1] > nums[size-2]:
            return (size - 1)
        
        #Binary search for the rest of the elements
        start = 1
        end = size - 2

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] > nums[mid-1]:
                start = mid+1
            
            elif nums[mid-1] > nums[mid]:
                end = mid-1
```