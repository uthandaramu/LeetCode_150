from collections import deque


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
        if not root:
            return root

        stack = deque()
        stack.append(root)

        while stack:
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

            if stack:
                top = stack[-1]
                cur.right = top

            cur.left = None