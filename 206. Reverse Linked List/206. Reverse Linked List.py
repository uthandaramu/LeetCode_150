# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        prev_node = None
        while head:
            cur_node = ListNode(head.val)
            cur_node.next = prev_node
            prev_node = cur_node

            head = head.next

        return prev_node