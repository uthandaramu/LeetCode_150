### 102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" width="200">

Input: root = [3,9,20,null,null,15,7]  
Output: [[3],[9,20],[15,7]]

**Example 2:**

Input: root = [1]  
Output: [[1]]

**Example 3:**

Input: root = []  
Output: []
 

**Constraints:**

* The number of nodes in the tree is in the range [0, 2000].
* -1000 <= Node.val <= 1000

### Own Approach (Less Readability)

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []

        queue = deque()

        queue.append((root, 0))

        tempSpace, idx = [], 0

        while queue:
            node, level = queue.popleft()

            if level == idx+1:
                result.append(tempSpace)
                tempSpace = []
                idx += 1
            
            tempSpace.append(node.val)
            
            if node.left:
                queue.append((node.left, level+1))
            
            if node.right:
                queue.append((node.right, level+1))

        result.append(tempSpace)

        return result
```

### Preferable Approach (Better Readability)

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []

        queue = deque()
        queue.append(root)

        while queue:
            tempSpace=[]
            width = len(queue)

            for _ in range(width):
                node = queue.popleft()
                tempSpace.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            result.append(tempSpace)

        return result
```