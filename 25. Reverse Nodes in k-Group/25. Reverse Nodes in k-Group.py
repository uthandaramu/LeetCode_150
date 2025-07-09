# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        ptr = head
        prev = None
        while ptr:
            tempNext = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tempNext

        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 1: return head

        ptr = groupFirst = head
        count = 0

        while ptr:
            count += 1
            if count == k:
                # Taking backup of ptr Next
                ptrNext = ptr.next

                # making this group end points to None
                ptr.next = None

                # reverse the group
                revGroup = self.reverseList(groupFirst)

                # Alter the head for first group
                if groupFirst == head:
                    head = revGroup
                else:
                    # for group other than first, connect with previous group end
                    prevGroupLast.next = revGroup

                # remembering previous group end
                prevGroupLast = groupFirst
                count = 0

                # moving to next group
                groupFirst = ptr = ptrNext

            else:
                ptr = ptr.next

        if count:
            # if there is still count, joining previous group end and unfinished last group first element
            prevGroupLast.next = groupFirst

        return (head)