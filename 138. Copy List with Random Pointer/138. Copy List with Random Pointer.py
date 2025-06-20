"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        hash_dict = {}
        ptr = head
        while ptr:
            hash_dict[ptr] = Node(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr:
            copy_node = hash_dict[ptr]
            if ptr.next:
                copy_node.next = hash_dict[ptr.next]
            if ptr.random:
                copy_node.random = hash_dict[ptr.random]
            ptr = ptr.next

        return hash_dict[head]