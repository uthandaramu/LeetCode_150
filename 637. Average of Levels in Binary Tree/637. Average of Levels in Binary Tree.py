from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        TreeQ = deque()
        TreeQ.append(root)

        result = []

        while TreeQ:
            level = len(TreeQ)
            total = 0
            for _ in range(level):

                node = TreeQ.popleft()
                total += node.val

                if node.left:
                    TreeQ.append(node.left)

                if node.right:
                    TreeQ.append(node.right)

            result.append(total / float(level))

        return result