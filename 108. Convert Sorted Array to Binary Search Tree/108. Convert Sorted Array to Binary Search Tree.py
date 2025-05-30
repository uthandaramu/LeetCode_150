# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        size = len(nums)
        if size == 1:
            node = TreeNode(nums[0])
            return node

        def rec_node(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = rec_node(start, mid - 1)
            root.right = rec_node(mid + 1, end)
            return root

        x = rec_node(0, size - 1)
        return x
