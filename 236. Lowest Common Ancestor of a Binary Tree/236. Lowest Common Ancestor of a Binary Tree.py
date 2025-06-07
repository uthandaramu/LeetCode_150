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