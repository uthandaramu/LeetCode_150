### 226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg" width="350">

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg" width="350">

**Input:** root = [2,1,3]
**Output:** [2,3,1]

**Example 3:**

**Input:** root = []  
**Output:** []

**Constraints:**

* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def invertTree(node):

            if not node or (not node.left and not node.right):
                return
            
            node.left, node.right = node.right, node.left

            invertTree(node.left)
            invertTree(node.right)
        
        invertTree(root)

        return root
```