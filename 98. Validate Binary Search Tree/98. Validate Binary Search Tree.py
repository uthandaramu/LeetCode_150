# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        inOrder = []

        stack_box = []
        ptr = root

        while stack_box or ptr:
            while ptr:
                stack_box.append(ptr)
                ptr = ptr.left

            ptr = stack_box.pop()
            if inOrder and inOrder[-1] >= ptr.val:
                return False
            inOrder.append(ptr.val)
            ptr = ptr.right

        return True