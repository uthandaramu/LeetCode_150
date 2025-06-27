### 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

**Example 1:**

Input: nums = [10,9,2,5,3,7,101,18]  
Output: 4  
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

**Example 2:**

Input: nums = [0,1,0,3,2,3]  
Output: 4

**Example 3:**

Input: nums = [7,7,7,7,7,7,7]  
Output: 1
 
**Constraints:**

* 1 <= nums.length <= 2500
* -104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subArr = [nums[0]]
        size = len(nums)

        for i in range(1, size):
            
            #Place nums in incremental order
            if nums[i] > subArr[-1]:
                subArr.append(nums[i])

            else:
                #If not find the place to replace the element i.e., find the lower bound position
                start = 0
                end = len(subArr)

                while start <= end:
                    mid = (start + end) // 2
                    if nums[i] <= subArr[mid]:
                        end = mid - 1
                        idx = mid
                    else:
                        start = mid + 1

                subArr[idx] = nums[i]
            
        return len(subArr)
```