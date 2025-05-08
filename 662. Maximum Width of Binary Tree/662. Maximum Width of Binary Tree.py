from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        box = deque()
        box.append((root, 1))
        maxWidth = 0
        while box:
            maxWidth = max(maxWidth, box[-1][1] - box[0][1] +1 )
            for _ in range(len(box)):
                node, idx = box.popleft()
                if node.left:
                    box.append((node.left, 2*idx))
                if node.right:
                    box.append((node.right, 2*idx+1))
        return maxWidth
