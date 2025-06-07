### 230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" width="200">

Input: root = [3,1,4,null,2], k = 1  
Output: 1  

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" width="200">

Input: root = [5,3,6,2,4,null,null,1], k = 3  
Output: 3  

**Constraints:**

The number of nodes in the tree is n.  
1 <= k <= n <= 104  
0 <= Node.val <= 104  

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = k
        self.out = None

        def in_order(r_node):
            if self.out is not None or r_node is None:
                return
            in_order(r_node.left)
            self.count -= 1
            if self.count == 0:
                self.out = r_node.val
                return
            in_order(r_node.right)

        in_order(root)
        return (self.out)
```