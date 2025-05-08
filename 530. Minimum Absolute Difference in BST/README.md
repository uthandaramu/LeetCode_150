### 530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" alt="Alt text" width="200"/>

Input: root = [4,2,6,1,3]  
Output: 1  

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" alt="Alt text" width="200"/>

Input: root = [1,0,48,null,null,12,49]  
Output: 1  

**Constraints:**

The number of nodes in the tree is in the range [2, 104].  
0 <= Node.val <= 105

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_val = float("inf")
        self.prev_val = None

        def diff(node):
            if not node:
                return
            diff(node.left)
            if self.prev_val is not None:
                self.min_val = min(self.min_val, abs(node.val - self.prev_val))
            self.prev_val = node.val
            diff(node.right)


        diff(root)
        return self.min_val
```