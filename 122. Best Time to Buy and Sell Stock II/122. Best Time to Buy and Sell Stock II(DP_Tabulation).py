class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[0 for _ in range(2)] for _ in range(size + 1)]

        dp_arr[size][0] = dp_arr[size][1] = 0

        for idx in range(size - 1, -1, -1):
            for buy_flag in range(0, 2):

                if buy_flag:
                    profit = max((-prices[idx] + dp_arr[idx + 1][0]), (dp_arr[idx + 1][1]))
                else:
                    profit = max((prices[idx] + dp_arr[idx + 1][1]), (dp_arr[idx + 1][0]))

                dp_arr[idx][buy_flag] = profit

        return dp_arr[0][1]