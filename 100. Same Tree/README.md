100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.  

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


**Example 1:**

<img src = "https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg">

Input: p = [1,2,3], q = [1,2,3]  
Output: true


**Example 2:**

<img src = "https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" width = 200>

Input: p = [1,2], q = [1,null,2]  
Output: false

**Example 3:**

<img src = "https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" >

Input: p = [1,2,1], q = [1,1,2]  
Output: false
 

**Constraints:**

The number of nodes in both trees is in the range [0, 100].  
-104 <= Node.val <= 104

### Depth First Search

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p or not q:
            return p == q
        
        return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)
```

### Breath First Search

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue_box = deque()
        queue_box.append((p, q))

        while queue_box:
            p_node, q_node = queue_box.popleft() 
            if not p_node and not q_node:
                continue
            if not q_node or not p_node or p_node.val != q_node.val :
                return False
            queue_box.append((p_node.left, q_node.left))
            queue_box.append((p_node.right, q_node.right))
        
        return True
```