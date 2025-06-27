class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        prev_arr = [[0 for _ in range(k + 1)] for _ in range(2)]

        for idx in range(size - 1, -1, -1):
            cur_arr = [[0 for _ in range(k + 1)] for _ in range(2)]
            for buy_flag in range(2):
                for cap in range(1, k + 1):
                    if buy_flag:
                        profit = max(-prices[idx] + prev_arr[0][cap], prev_arr[1][cap])
                    else:
                        profit = max(prices[idx] + prev_arr[1][cap - 1], prev_arr[0][cap])

                    cur_arr[buy_flag][cap] = profit

            prev_arr = cur_arr

        return prev_arr[1][k]