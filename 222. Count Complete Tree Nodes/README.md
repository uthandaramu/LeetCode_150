### 222. Count Complete Tree Nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

**Example 1:**


Input: root = [1,2,3,4,5,6]  
Output: 6  

**Example 2:**

Input: root = []  
Output: 0

**Example 3:**

Input: root = [1]  
Output: 1
 

**Constraints:**

The number of nodes in the tree is in the range [0, 5 * 104].  
0 <= Node.val <= 5 * 104  
The tree is guaranteed to be complete.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def count_left_height(self, node):
        count = 0
        while (node.left is not None):
                count += 1
                node = node.left
        return count + 1

    def count_right_height(self, node):
        count = 0
        while (node.right is not None):
                count += 1
                node = node.right
        return count + 1

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        left_height = right_height = 0
        ptr = root
        if not root:
            return 0
        left_height = self.count_left_height(ptr)
        right_height = self.count_right_height(ptr)
        
        if left_height == right_height:
            return (2**left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    
```