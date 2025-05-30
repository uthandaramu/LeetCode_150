class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        def rec_trade(idx, buy_flag, cap):
            if idx == size or cap == 0:
                return 0
            if buy_flag:
                profit = max(-prices[idx] + rec_trade(idx + 1, 0, cap), rec_trade(idx + 1, 1, cap))
            else:
                profit = max(prices[idx] + rec_trade(idx + 1, 1, cap - 1), rec_trade(idx + 1, 0, cap))

            return profit

        x = rec_trade(0, 1, 2)
        return x