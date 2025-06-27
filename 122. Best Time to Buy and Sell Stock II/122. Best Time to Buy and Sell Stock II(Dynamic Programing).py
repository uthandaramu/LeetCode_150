class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[-1 for _ in range(2)] for _ in range(size)]

        def rec_trade(idx, buy_flag):
            if idx == size:
                return 0
            if dp_arr[idx][buy_flag] == -1:
                if buy_flag:
                    profit = max((-prices[idx] + rec_trade(idx + 1, 0)), (rec_trade(idx + 1, 1)))
                else:
                    profit = max((prices[idx] + rec_trade(idx + 1, 1)), (rec_trade(idx + 1, 0)))

                dp_arr[idx][buy_flag] = profit

            return dp_arr[idx][buy_flag]

        x = rec_trade(0, 1)
        return x