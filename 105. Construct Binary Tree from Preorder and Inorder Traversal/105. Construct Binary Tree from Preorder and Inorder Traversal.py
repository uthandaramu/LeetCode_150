from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderIndexHash = defaultdict(int)

        size = len(inorder)

        for i in range(size):
            inorderIndexHash[inorder[i]] = i

        def constructTree(inStart, inEnd, preStart, preEnd):

            if (inStart > inEnd) or (preStart > preEnd):
                return None

            node = TreeNode(preorder[preStart])

            # Left Nodes
            nodeIndex = inorderIndexHash[preorder[preStart]]
            leftNodeCount = nodeIndex - inStart

            node.left = constructTree(inStart, inStart + leftNodeCount, preStart + 1, preStart + leftNodeCount)

            # Right Nodes
            node.right = constructTree(nodeIndex + 1, inEnd, preStart + leftNodeCount + 1, preEnd)

            return node

        return (constructTree(0, size - 1, 0, size - 1))