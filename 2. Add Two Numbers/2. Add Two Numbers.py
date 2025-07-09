# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy_node = res_ptr = ListNode(-1)

        while ptr1 or ptr2:
            val1 = 0 if not ptr1 else ptr1.val
            val2 = 0 if not ptr2 else ptr2.val
            res = val1 + val2

            if carry:
                res += carry
                carry = 0

            if res > 9:
                carry = 1
                res = res % 10

            res_ptr.next = ListNode(res)
            res_ptr = res_ptr.next
            if ptr1: ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next

        if carry:
            res_ptr.next = ListNode(carry)

        return dummy_node.next