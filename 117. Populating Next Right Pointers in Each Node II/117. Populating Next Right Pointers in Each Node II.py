from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        storage_stack = deque()
        storage_stack.append(root)

        while storage_stack:
            prev_node = None
            for _ in range(len(storage_stack)):
                node = storage_stack.popleft()

                if prev_node:
                    prev_node.next = node
                prev_node = node

                if node.left:
                    storage_stack.append(node.left)
                if node.right:
                    storage_stack.append(node.right)

        return root