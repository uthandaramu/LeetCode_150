### 236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png">

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  
Output: 3  
Explanation: The LCA of nodes 5 and 1 is 3.

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png">

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4  
Output: 5  
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

**Example 3:**

Input: root = [1,2], p = 1, q = 2  
Output: 1

**Constraints:**

The number of nodes in the tree is in the range [2, 105].  
-109 <= Node.val <= 109  
All Node.val are unique.  
p != q  
p and q will exist in the tree.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs_lca(node):
            if not node:
                return
            if node == p:
                return node
            if node == q:
                return node
    
            left_res = dfs_lca(node.left)
            right_res = dfs_lca(node.right)

            if not left_res and not right_res:
                return None
            elif left_res and right_res:
                return node
            else:
                return (left_res or right_res)
        
        x = dfs_lca(root)
        return x
```