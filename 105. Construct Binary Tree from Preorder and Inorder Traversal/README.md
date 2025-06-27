### 105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

**Example 1**:

<img src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" width="200">

**Input:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  
**Output:** [3,9,20,null,null,15,7]

**Example 2:**

**Input:** preorder = [-1], inorder = [-1]  
**Output:** [-1]
 

**Constraints:**

* 1 <= preorder.length <= 3000
* inorder.length == preorder.length
* -3000 <= preorder[i], inorder[i] <= 3000
* preorder and inorder consist of unique values.
* Each value of inorder also appears in preorder.
* preorder is guaranteed to be the preorder traversal of the tree.
* inorder is guaranteed to be the inorder traversal of the tree.

```python
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

            #Left Nodes
            nodeIndex = inorderIndexHash[preorder[preStart]]
            leftNodeCount = nodeIndex - inStart

            node.left = constructTree(inStart, inStart + leftNodeCount, preStart+1, preStart+leftNodeCount)

            #Right Nodes
            node.right = constructTree(nodeIndex+1, inEnd, preStart+leftNodeCount+1, preEnd)
        
            return node
        
        return (constructTree(0, size-1, 0, size-1))
```