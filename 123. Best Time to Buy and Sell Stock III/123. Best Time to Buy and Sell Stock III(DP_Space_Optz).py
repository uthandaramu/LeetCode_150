class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        prev_arr = [[0 for _ in range(3)] for _ in range(2)]

        for idx in range(size - 1, -1, -1):
            cur_arr = [[0 for _ in range(3)] for _ in range(2)]

            for buy_flag in range(2):
                for cap in range(1, 3):

                    if buy_flag:
                        target = max(-prices[idx] + prev_arr[0][cap], prev_arr[1][cap])
                    else:
                        target = max(prices[idx] + prev_arr[1][cap - 1], prev_arr[0][cap])

                    cur_arr[buy_flag][cap] = target

            prev_arr = cur_arr

        return prev_arr[1][2]