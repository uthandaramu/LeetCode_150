import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []

        for val in nums:
            if len(min_heap) <= k:
                heapq.heappush(min_heap, val)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return (heapq.heappop(min_heap))