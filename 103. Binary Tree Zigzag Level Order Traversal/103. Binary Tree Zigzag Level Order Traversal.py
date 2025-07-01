from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result, flag = [], 0
        treeQ = deque()
        treeQ.append(root)

        while treeQ:
            tempArr = []
            for _ in range(len(treeQ)):
                node = treeQ.popleft()
                tempArr.append(node.val)

                if node.left:
                    treeQ.append(node.left) 
                
                if node.right:
                    treeQ.append(node.right)

            if flag:
                tempArr.reverse()
            
            flag = not(flag)

            result.append(tempArr)

        return (result)