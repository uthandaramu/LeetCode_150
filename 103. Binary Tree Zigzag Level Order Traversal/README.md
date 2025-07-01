### 103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

**Example 1:**

<img src = "https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" width = "200">

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** [[3],[20,9],[15,7]]

**Example 2:**

**Input:** root = [1]  
**Output:** [[1]]

**Example 3:**

**Input:** root = []  
**Output:** []
 

**Constraints:**

* The number of nodes in the tree is in the range [0, 2000].
* -100 <= Node.val <= 100

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result, flag = [], 0
        treeQ = deque()
        treeQ.append(root)

        while treeQ:
            tempArr = []
            for _ in range(len(treeQ)):
                node = treeQ.popleft()
                tempArr.append(node.val)

                if node.left:
                    treeQ.append(node.left) 
                
                if node.right:
                    treeQ.append(node.right)

            if flag:
                tempArr.reverse()
            
            flag = not(flag)

            result.append(tempArr)

        return (result)
```