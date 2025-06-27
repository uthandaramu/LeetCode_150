from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        size = len(inorder)

        inorderIndexHash = defaultdict(int)

        for i in range(size):
            inorderIndexHash[inorder[i]] = i

        def constructTree(inStart, inEnd, postStart, postEnd):

            if (inStart > inEnd) or (postStart > postEnd):
                return None

            node = TreeNode(postorder[postEnd])

            # Left Nodes
            nodeIndex = inorderIndexHash[postorder[postEnd]]
            leftNodesNum = nodeIndex - inStart

            node.left = constructTree(inStart, inStart + leftNodesNum, postStart, postStart + leftNodesNum - 1)

            # Right Nodes
            node.right = constructTree(nodeIndex + 1, inEnd, postStart + leftNodesNum, postEnd - 1)

            return node

        return (constructTree(0, size - 1, 0, size - 1))