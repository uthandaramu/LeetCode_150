# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_val = float("inf")
        self.prev_val = None

        def diff(node):
            if not node:
                return
            diff(node.left)
            if self.prev_val is not None:
                self.min_val = min(self.min_val, abs(node.val - self.prev_val))
            self.prev_val = node.val
            diff(node.right)

        diff(root)
        return self.min_val
