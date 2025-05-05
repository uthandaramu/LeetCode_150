# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2
        dummy_node = out_ll = ListNode(-1)
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val < ptr2.val:
                    dummy_node.next = ptr1
                    ptr1 = ptr1.next
                else:
                    dummy_node.next = ptr2
                    ptr2 = ptr2.next

                dummy_node = dummy_node.next
            elif ptr1:
                dummy_node.next = ptr1
                ptr1 = None
            elif ptr2:
                dummy_node.next = ptr2
                ptr2 = None

        return out_ll.next