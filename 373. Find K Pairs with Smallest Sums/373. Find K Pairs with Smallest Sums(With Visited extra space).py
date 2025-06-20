import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        out = []
        size1 = len(nums1)
        size2 = len(nums2)

        # To avoid repeatative combinations
        visited = set()

        i = j = 0
        minHeap = []

        # To keep a track of minimum sum combinations
        heapq.heappush(minHeap, (nums1[0] + nums2[0], 0, 0))

        out = []

        count = 0

        while minHeap and (i < size1 or j < size2) and count < k:

            total, first, second = heapq.heappop(minHeap)
            out.append([nums1[first], nums2[second]])

            # (i+1, j) combination
            if (first + 1, second) not in visited and first + 1 < size1:
                total = nums1[first + 1] + nums2[second]
                heapq.heappush(minHeap, (total, first + 1, second))
                visited.add((first + 1, second))

            # (i, j+1) combination
            if (first, second + 1) not in visited and second + 1 < size2:
                total = nums1[first] + nums2[second + 1]
                heapq.heappush(minHeap, (total, first, second + 1))
                visited.add((first, second + 1))

            # Tracking K values
            count += 1

        return (out)