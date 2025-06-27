238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Example 1:**

Input: nums = [1,2,3,4]  
Output: [24,12,8,6]

**Example 2:**

Input: nums = [-1,1,0,-3,3]  
Output: [0,0,9,0,0]  
 

**Constraints:**

* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.  

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

### With Extra Space

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        prefix = [1 for _ in range(size)]
        postfix = [1 for _ in range(size)]
        out = [1 for _ in range(size)]
        
        #prefix operation
        for i in range(size):
            prefix[i] = prefix[i-1] * nums[i]

        postfix[size-1] = nums[size-1]

        for j in range(size-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j]
        
        for i in range(size):
            if i == 0:
                out[i] = postfix[i+1]
            elif i == size-1:
                out[i] = prefix[i-1]
            else:
                out[i] = prefix[i-1] * postfix[i+1]
        
        return (out)
```

### Without Extra Space

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)

        out = [1 for _ in range(size)]
        
        #Prefix operation
        pre = 1
        out[0] = pre
        for i in range(1, size):
            out[i] = pre * nums[i-1]
            pre = out[i]
        
        #Postfix operation
        post = 1
        for i in range(size-1, -1, -1):
            out[i] = post * out[i]
            post = post * nums[i]
        
        return (out)
```