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