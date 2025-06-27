import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        size1 = len(nums1)
        size2 = len(nums2)

        minHeap = []

        #Add all elements in first array paring with oth index element in second array
        i = 0
        while i < size1 and i < k:
            total = nums1[i] + nums2[0]
            heapq.heappush(minHeap, (total, i, 0))
            i += 1

        count = 0
        out = []
        while heapq and count < k:

            total, i, j = heapq.heappop(minHeap)
            out.append([nums1[i], nums2[j]])

            #Since we have all first array elements in pair, it is required to iterate elements in second array which can avoid duplicate paring
            if j + 1 < size2:
                total = nums1[i] + nums2[j + 1]
                heapq.heappush(minHeap, (total, i, j + 1))

            count += 1

        return (out)