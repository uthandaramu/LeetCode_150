# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def invertTree(node):
            if not node or (not node.left and not node.right):
                return

            node.left, node.right = node.right, node.left

            invertTree(node.left)
            invertTree(node.right)

        invertTree(root)

        return root