# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def rec_PathSum(node, localSum):
            if not node:
                return False

            localSum += node.val

            if not node.left and not node.right:
                return localSum == targetSum

            return (rec_PathSum(node.left, localSum) or rec_PathSum(node.right, localSum))

        return rec_PathSum(root, 0)