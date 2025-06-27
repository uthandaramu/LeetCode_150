### 215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

**Example 1:**

Input: nums = [3,2,1,5,6,4], k = 2  
Output: 5

**Example 2:**

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4  
Output: 4

**Constraints:**

1 <= k <= nums.length <= 105  
-104 <= nums[i] <= 104

### With Quick Select Technique

#### (May cause TLE as Time Complexity: Average[O(n)] Worst[O(n^2)])

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        target_index = size - k

        # Quick Select Approach (using array partioning)
        def rec_k(start, end):
            pivot = end
            pointer = start

            for idx in range(start, end):
                if nums[idx] <= nums[pivot]:
                    nums[idx], nums[pointer] = nums[pointer], nums[idx]
                    pointer += 1

            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]

            if pointer == (size-k):
                return nums[pointer]
            elif pointer > (size-k):
                return rec_k(start, pointer-1)
            else:
                return rec_k(pointer+1, end)
            

        return (rec_k(0, size-1))        
```

#### With Priority Queue (Heap data structure)

```python
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []

        for val in nums:
            if len(min_heap) <= k:
                heapq.heappush(min_heap, val)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return (heapq.heappop(min_heap))                  
```