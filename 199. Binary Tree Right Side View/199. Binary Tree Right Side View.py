# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out_arr = []

        # Modified pre order traversal as (right, left, root)
        def rec_pre_order(node, level):
            if not node:
                return
            if len(out_arr) == level:
                out_arr.append(node.val)
            rec_pre_order(node.right, level + 1)
            rec_pre_order(node.left, level + 1)

        rec_pre_order(root, 0)
        return out_arr