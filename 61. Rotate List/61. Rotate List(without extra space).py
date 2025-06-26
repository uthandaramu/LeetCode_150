# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        length = count = 0
        ptr = head

        while ptr:
            tail = ptr
            length += 1
            ptr = ptr.next

        tail.next = head

        idxToRotate = length - (k % length)

        ptr = head
        start = None
        while count <= idxToRotate - 1:
            count += 1
            start = ptr
            ptr = ptr.next

        if start:
            head = start.next
            start.next = None

        return head