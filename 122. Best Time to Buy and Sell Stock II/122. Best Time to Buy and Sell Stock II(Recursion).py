class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        def rec_trade(idx, buy_flag):
            if idx == size:
                return 0
            if buy_flag:
                profit = max((-prices[idx] + rec_trade(idx + 1, 0)), (rec_trade(idx + 1, 1)))
            else:
                profit = max((prices[idx] + rec_trade(idx + 1, 1)), (rec_trade(idx + 1, 0)))

            return profit

        x = rec_trade(0, 1)
        return x