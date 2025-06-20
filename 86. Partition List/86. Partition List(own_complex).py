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
        if not head:
            return head

        dummy_node = ListNode(-1, head)
        cur_ptr = head
        less_prev = high_prev = dummy_node

        first_high = None

        while cur_ptr:
            if cur_ptr.val < x:
                less_prev.next = cur_ptr
                less_prev = cur_ptr
            else:
                if not first_high:
                    first_high = cur_ptr
                    high_prev = first_high
                else:
                    high_prev.next = cur_ptr
                    high_prev = cur_ptr

            cur_ptr = cur_ptr.next

        less_prev.next = first_high
        if first_high:
            high_prev.next = cur_ptr

        return dummy_node.next