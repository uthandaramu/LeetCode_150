import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        size = len(lists)

        minHeap = []

        for i in range(size):
            if lists[i]:
                val = lists[i].val
                heapq.heappush(minHeap, (val, lists[i]))

        dummy_node = out_ptr = ListNode(-1)

        while minHeap:

            _, top_node = heapq.heappop(minHeap)
            out_ptr.next = top_node
            if top_node.next:
                val = top_node.next.val
                heapq.heappush(minHeap, (val, top_node.next))

            out_ptr = out_ptr.next

        return dummy_node.next