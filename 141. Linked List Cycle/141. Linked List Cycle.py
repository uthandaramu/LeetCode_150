# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Algorithm = Tortise and Hare (slow and fast)
        # Intituion: if ther is a loop, and fast moves towards slow by two and slow moves away by 1, the net Distance will gets reduced by 1 and eventually the distance become 0

        slow = fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False