from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []

        queue = deque()

        queue.append((root, 0))

        tempSpace, idx = [], 0

        while queue:
            node, level = queue.popleft()

            if level == idx + 1:
                result.append(tempSpace)
                tempSpace = []
                idx += 1

            tempSpace.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        result.append(tempSpace)

        return result