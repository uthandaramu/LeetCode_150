# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def count_left_height(self, node):
        count = 0
        while (node.left is not None):
            count += 1
            node = node.left
        return count + 1

    def count_right_height(self, node):
        count = 0
        while (node.right is not None):
            count += 1
            node = node.right
        return count + 1

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        left_height = right_height = 0
        ptr = root
        if not root:
            return 0
        left_height = self.count_left_height(ptr)
        right_height = self.count_right_height(ptr)

        if left_height == right_height:
            return (2 ** left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
