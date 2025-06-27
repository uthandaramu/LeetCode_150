class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(size + 1)]

        for idx in range(size - 1, -1, -1):
            for buy_flag in range(2):
                for cap in range(1, k + 1):
                    if buy_flag:
                        profit = max(-prices[idx] + dp_arr[idx + 1][0][cap], dp_arr[idx + 1][1][cap])
                    else:
                        profit = max(prices[idx] + dp_arr[idx + 1][1][cap - 1], dp_arr[idx + 1][0][cap])

                    dp_arr[idx][buy_flag][cap] = profit

        return dp_arr[0][1][k]