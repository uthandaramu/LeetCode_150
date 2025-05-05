# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middle(self, ll_list):
        slow_ptr = ll_list
        fast_ptr = ll_list.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

    def ll_sort_merge(self, a_list, b_list):
        dummy_list = out_ptr = ListNode(-1)
        while a_list and b_list:
            if a_list.val < b_list.val:
                dummy_list.next = a_list
                a_list = a_list.next
            else:
                dummy_list.next = b_list
                b_list = b_list.next
            dummy_list = dummy_list.next

        if a_list:
            dummy_list.next = a_list

        if b_list:
            dummy_list.next = b_list

        return out_ptr.next

    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        left = head
        mid = self.middle(head)
        tmp = mid.next
        mid.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.ll_sort_merge(left, right)
