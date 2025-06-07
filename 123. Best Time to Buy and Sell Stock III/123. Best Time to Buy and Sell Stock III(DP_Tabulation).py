class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(size + 1)]

        for idx in range(size - 1, -1, -1):
            for buy_flag in range(2):
                for cap in range(1, 3):

                    if buy_flag:
                        target = max(-prices[idx] + dp_arr[idx + 1][0][cap], dp_arr[idx + 1][1][cap])
                    else:
                        target = max(prices[idx] + dp_arr[idx + 1][1][cap - 1], dp_arr[idx + 1][0][cap])

                    dp_arr[idx][buy_flag][cap] = target

        return dp_arr[0][1][2]