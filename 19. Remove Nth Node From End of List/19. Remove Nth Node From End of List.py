# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        ptr = head
        length = 0
        while ptr:
            length+=1
            ptr = ptr.next
        if length == n:
            head = head.next
            return head
        ptr = head
        el_index = length - n
        count = 1
        while ptr:
            if count == el_index:
                if count == length-1:
                    ptr.next = None
                    return head
                else:
                    ptr.next = ptr.next.next
                    return head
            ptr = ptr.next
            count += 1 