from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        top_element = self.stack.pop()
        out_val = top_element.val
        if top_element.right:
            top_element = top_element.right
            while top_element:
                self.stack.append(top_element)
                top_element = top_element.left
        return out_val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()