### 98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.  
* The right subtree of a node contains only nodes with keys greater than the node's key.  
* Both the left and right subtrees must also be binary search trees.  
 

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" width="250">

Input: root = [2,1,3]  
Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" width="250">

Input: root = [5,1,4,null,null,3,6]  
Output: false  
Explanation: The root node's value is 5 but its right child's value is 4.

**Constraints:**

* The number of nodes in the tree is in the range [1, 104].
* -231 <= Node.val <= 231 - 1

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        inOrder = []

        stack_box = []
        ptr = root

        while stack_box or ptr:
            while ptr:
                stack_box.append(ptr)
                ptr = ptr.left
            
            ptr = stack_box.pop()
            if inOrder and inOrder[-1] >= ptr.val:
                return False
            inOrder.append(ptr.val)
            ptr = ptr.right
        
        return True
```