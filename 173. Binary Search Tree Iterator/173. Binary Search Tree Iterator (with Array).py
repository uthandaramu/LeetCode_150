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
        self.tree_arr = self.lastNode(root)
        self.size = len(self.tree_arr)
        self.ptr = 0

    def next(self):
        """
        :rtype: int
        """
        out = self.tree_arr[self.ptr].val
        self.ptr += 1
        return out

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ptr < self.size:
            return True
        else:
            return False

    def lastNode(self, root):
        tree_arr = []
        if root.left:
            tree_arr += (self.lastNode(root.left))
        tree_arr.append(root)
        if root.right:
            tree_arr += (self.lastNode(root.right))
        return tree_arr

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()