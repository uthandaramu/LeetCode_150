101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" alt="Alt text" width="200"/>

Input: root = [1,2,2,3,4,4,3]  
Output: true  

**Example 2:**  

<img src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" alt="Alt text" width="200"/>

Input: root = [1,2,2,null,3,null,3]    
Output: false

**Constraints:**

The number of nodes in the tree is in the range [1, 1000].  
-100 <= Node.val <= 100  

Follow up: Could you solve it both recursively and iteratively?

### Recursive Approach

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helpSymmetric(ptr1, ptr2):

            if ptr1 == None or ptr2 == None:
                return ptr1 == ptr2

            if ptr1.val != ptr2.val:
                return False
            
            return (helpSymmetric(ptr1.left, ptr2.right) and (helpSymmetric(ptr1.right, ptr2.left)))
        
        return root == None or helpSymmetric(root.left, root.right)
            
```
### Iterative Approach (Level Order Traversal)

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack1 = deque()
        stack2 = deque()
        if not root:
            return True
        stack1.appendleft(root.left)
        stack2.appendleft(root.right)
        cur_el_1 = cur_el_2 = None
        while stack1 and stack2:
            cur_el_1 = stack1.pop()
            cur_el_2 = stack2.pop()
            if cur_el_1 == None and cur_el_2 == None:
                continue
            if cur_el_1 == None or cur_el_2 == None:
                return False
            if cur_el_1.val != cur_el_2.val:
                return False

            stack1.appendleft(cur_el_1.left)
            stack1.appendleft(cur_el_1.right)
            stack2.appendleft(cur_el_2.right)
            stack2.appendleft(cur_el_2.left)

        return not stack1 and not stack2
```