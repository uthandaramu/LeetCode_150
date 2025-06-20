### 106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" width="250">

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]  
Output: [3,9,20,null,null,15,7]

**Example 2:**

Input: inorder = [-1], postorder = [-1]  
Output: [-1]
 

**Constraints:**

* 1 <= inorder.length <= 3000
* postorder.length == inorder.length
* -3000 <= inorder[i], postorder[i] <= 3000
* inorder and postorder consist of unique values.
* Each value of postorder also appears in inorder.
* inorder is guaranteed to be the inorder traversal of the tree.
* postorder is guaranteed to be the postorder traversal of the tree.

```python
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

            #Left Nodes
            nodeIndex = inorderIndexHash[postorder[postEnd]]
            leftNodesNum = nodeIndex - inStart

            node.left = constructTree(inStart, inStart + leftNodesNum, postStart, postStart + leftNodesNum-1)

            #Right Nodes
            node.right = constructTree(nodeIndex +1, inEnd, postStart + leftNodesNum, postEnd - 1 )
            
            return node
        
        return (constructTree(0, size-1, 0, size-1))
```