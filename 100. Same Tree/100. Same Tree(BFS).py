from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue_box = deque()
        queue_box.append((p, q))

        while queue_box:
            p_node, q_node = queue_box.popleft() 
            if not p_node and not q_node:
                continue
            if not q_node or not p_node or p_node.val != q_node.val :
                return False
            queue_box.append((p_node.left, q_node.left))
            queue_box.append((p_node.right, q_node.right))
        
        return True