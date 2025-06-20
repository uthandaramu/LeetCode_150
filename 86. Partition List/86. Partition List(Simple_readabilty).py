# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        left_node = left_ptr = ListNode(0)
        right_node = right_ptr = ListNode(0)

        while head:
            if head.val < x:
                left_node.next = head
                left_node = left_node.next
            else:
                right_node.next = head
                right_node = right_node.next

            head = head.next

        right_node.next = None
        left_node.next = right_ptr.next

        return left_ptr.next