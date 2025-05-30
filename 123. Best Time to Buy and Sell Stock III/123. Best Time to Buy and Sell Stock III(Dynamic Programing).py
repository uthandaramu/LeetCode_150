class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(size)]

        def rec_trade(idx, buy_flag, cap):
            if idx == size or cap == 0:
                return 0
            if dp_arr[idx][buy_flag][cap] == -1:

                if buy_flag:
                    profit = max(-prices[idx] + rec_trade(idx + 1, 0, cap), rec_trade(idx + 1, 1, cap))
                else:
                    profit = max(prices[idx] + rec_trade(idx + 1, 1, cap - 1), rec_trade(idx + 1, 0, cap))

                dp_arr[idx][buy_flag][cap] = profit

            return dp_arr[idx][buy_flag][cap]

        x = rec_trade(0, 1, 2)
        return x