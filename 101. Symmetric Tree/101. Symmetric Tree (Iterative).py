from collections import deque
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
        stack1 = deque()
        stack2 = deque()
        if not root:
            return True
        stack1.appendleft(root.left)
        stack2.appendleft(root.right)
        cur_el_1 = cur_el_2 = None
        while stack1 and stack2:
            cur_el_1 = stack1.pop()
            cur_el_2 = stack2.pop()
            if cur_el_1 == None and cur_el_2 == None:
                continue
            if cur_el_1 == None or cur_el_2 == None:
                return False
            if cur_el_1.val != cur_el_2.val:
                return False

            stack1.appendleft(cur_el_1.left)
            stack1.appendleft(cur_el_1.right)
            stack2.appendleft(cur_el_2.right)
            stack2.appendleft(cur_el_2.left)

        return not stack1 and not stack2