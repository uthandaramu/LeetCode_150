class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = [0 for _ in range(len(citations) + 1)]
        for i in citations:
            if i > len(citations):
                i = len(citations)
            count[i] += 1
        h_index = 0
        print(count)
        for j in range(len(count) - 1, -1, -1):
            h_index += count[j]
            if h_index >= j:
                return j
