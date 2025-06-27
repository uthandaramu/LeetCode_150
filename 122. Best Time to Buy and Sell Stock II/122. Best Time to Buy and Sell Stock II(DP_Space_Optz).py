class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        prev_arr = [0 for _ in range(2)]

        for idx in range(size-1, -1, -1):
            cur_arr = [0 for _ in range(2)]
            for buy_flag in range(0, 2):
                if buy_flag:
                    profit = max((-prices[idx] + prev_arr[0]), (prev_arr[1]))
                else:
                    profit = max((prices[idx] + prev_arr[1]),(prev_arr[0]))

                cur_arr[buy_flag] = profit
            prev_arr = cur_arr

        return prev_arr[1]