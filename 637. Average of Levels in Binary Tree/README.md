### 637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" width="200">

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** [3.00000,14.50000,11.00000]  
**Explanation:** The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.  
Hence return [3, 14.5, 11].

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" width="200"> 

**Input:** root = [3,9,20,15,7]  
**Output:** [3.00000,14.50000,11.00000]

**Constraints:**

* The number of nodes in the tree is in the range [1, 104].
* -231 <= Node.val <= 231 - 1

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        TreeQ = deque()
        TreeQ.append(root)

        result = []

        while TreeQ:
            level = len(TreeQ)
            total = 0
            for _ in range(level):

                node = TreeQ.popleft()
                total += node.val

                if node.left:
                    TreeQ.append(node.left)
                
                if node.right:
                    TreeQ.append(node.right)

            result.append(total/float(level))
        
        return result
```