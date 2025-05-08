### 124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.  

The path sum of a path is the sum of the node's values in the path.    

Given the root of a binary tree, return the maximum path sum of any non-empty path.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" alt="Alt text" width="200"/>

Input: root = [1,2,3]  
Output: 6  
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" alt="Alt text" width="200"/>

Input: root = [-10,9,20,null,null,15,7]  
Output: 42  
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

**Constraints:**

The number of nodes in the tree is in the range [1, 3 * 104].  
-1000 <= Node.val <= 1000

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_sum = [root.val]
        def dfs(root):
            if not root:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            left_sum = max(0, left_sum)
            right_sum = max(0, right_sum)
            max_sum[0] = max(max_sum[0], root.val + left_sum + right_sum)

            return root.val + max(left_sum, right_sum)

        dfs(root)
        return max_sum[0]
```