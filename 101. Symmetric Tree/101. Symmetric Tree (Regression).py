# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def helpSymmetric(ptr1, ptr2):

            if ptr1 == None or ptr2 == None:
                return ptr1 == ptr2

            if ptr1.val != ptr2.val:
                return False

            return (helpSymmetric(ptr1.left, ptr2.right) and (helpSymmetric(ptr1.right, ptr2.left)))

        return root == None or helpSymmetric(root.left, root.right)
