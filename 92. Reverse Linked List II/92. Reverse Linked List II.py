# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        count = 1
        dummy_node = ListNode(0, head)
        leftPrev = dummy_node
        cur_node = head

        # Placing my left pointer in left index and prevLeft in previous to left
        for _ in range(left - 1):
            leftPrev, cur_node = cur_node, cur_node.next

        # breaking the next pointer and reversing the focus nodes
        prev = None
        for _ in range(right - left + 1):
            tempNext = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = tempNext

        # rejoining the reversed node with unaltered node
        leftPrev.next.next = cur_node
        leftPrev.next = prev

        return dummy_node.next