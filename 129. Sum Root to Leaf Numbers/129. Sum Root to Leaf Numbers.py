# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def rec_sum(node, result):
            if not node:
                return 0

            result = (result * 10) + node.val

            if not node.left and not node.right:
                return result

            return (rec_sum(node.left, result) + rec_sum(node.right, result))

        return (rec_sum(root, 0))