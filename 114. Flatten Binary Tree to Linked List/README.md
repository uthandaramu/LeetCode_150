### 114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

* The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
* The "linked list" should be in the same order as a pre-order traversal of the binary tree.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" width="350">

Input: root = [1,2,5,3,4,null,6]  
Output: [1,null,2,null,3,null,4,null,5,null,6]

**Example 2:**

Input: root = []  
Output: []

**Example 3:**

Input: root = [0]  
Output: [0]

**Constraints:**

* The number of nodes in the tree is in the range [0, 2000].
* -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
            
        stack = deque()
        stack.append(root)

        while stack:
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)
            
            if cur.left:
                stack.append(cur.left)
            
            if stack:
                top = stack[-1]
                cur.right = top
            
            cur.left = None
```

### Space Optimized and preferable

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        cur = root

        while cur:

            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right

                prev.right = cur.right
                
                cur.right = cur.left
                cur.left = None

            cur = cur.right
```