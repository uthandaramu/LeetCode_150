# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        cur = root

        while cur:

            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right

                prev.right = cur.right

                cur.right = cur.left
                cur.left = None

            cur = cur.right