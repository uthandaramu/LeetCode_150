### 199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1:**

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

<img src="https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png" width="300">

**Example 2:**

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

<img src="https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png" width="300">

**Example 3:**

Input: root = [1,null,3]

Output: [1,3]

**Example 4:**

Input: root = []

Output: []

**Constraints:**

The number of nodes in the tree is in the range [0, 100].  
-100 <= Node.val <= 100

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out_arr = []
        
        #Modified pre order traversal as (right, left, root)
        def rec_pre_order(node, level):
            if not node:
                return 
            if len(out_arr) == level:
                out_arr.append(node.val)
            rec_pre_order(node.right, level+1)
            rec_pre_order(node.left, level+1)
        
        rec_pre_order(root, 0)
        return out_arr
```