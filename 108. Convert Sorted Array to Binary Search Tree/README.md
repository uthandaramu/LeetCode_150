### 108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

**Example 1:**

Input: nums = [-10,-3,0,5,9]  
Output: [0,-3,9,-10,null,5]  
Explanation: [0,-10,5,null,-3,null,9] is also accepted:  

<img src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" width="200">

or

<img src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" width="200">

**Example 2:**

Input: nums = [1,3]  
Output: [3,1]  
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.  

<img src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" width="200">

**Constraints:**

1 <= nums.length <= 104  
-104 <= nums[i] <= 104  
nums is sorted in a strictly increasing order.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        size = len(nums)
        if size == 1:
            node = TreeNode(nums[0])
            return node

        def rec_node(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = rec_node(start, mid-1)
            root.right = rec_node(mid+1, end)
            return root
            
        x = rec_node(0, size-1)
        return x
```