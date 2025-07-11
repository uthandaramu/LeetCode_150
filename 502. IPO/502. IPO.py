import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        maxProfit = []  # Affordable maximum profits
        minCapital = [(cap, prof) for cap, prof in zip(capital, profits)]  # Non affordable capital

        heapq.heapify(minCapital)

        for i in range(k):

            while minCapital and minCapital[0][0] <= w:
                affordable = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -affordable[1])

            if not maxProfit:
                break
            w += (-heapq.heappop(maxProfit))

        return w