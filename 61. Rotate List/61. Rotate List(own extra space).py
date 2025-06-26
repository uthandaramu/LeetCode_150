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

        nodeIdx = {}

        count = 0

        ptr = out_ptr = head

        while ptr:
            nodeIdx[count] = ptr
            ptr = ptr.next
            count += 1

        rotate_num = k % count

        rotateNode = nodeIdx[count - rotate_num - 1]

        if rotateNode.next:
            tempNext = out_ptr = rotateNode.next
            rotateNode.next = None
            while tempNext.next:
                tempNext = tempNext.next

            tempNext.next = head

        return out_ptr