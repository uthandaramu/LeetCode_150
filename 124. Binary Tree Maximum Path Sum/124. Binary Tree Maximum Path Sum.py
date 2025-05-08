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