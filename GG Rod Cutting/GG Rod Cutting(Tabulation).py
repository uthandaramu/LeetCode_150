# User function Template for python3

class Solution:
    def cutRod(self, price):
        # code here

        size = len(price)

        dp_arr = [[0 for _ in range(size + 1)] for _ in range(size)]

        for cap in range(size + 1):
            dp_arr[0][cap] = (cap) * price[0]

        for idx in range(1, size):
            for capacity in range(size + 1):
                not_pick = dp_arr[idx - 1][capacity]
                pick = 0
                if capacity >= idx + 1:
                    pick = price[idx] + dp_arr[idx][capacity - (idx + 1)]
                dp_arr[idx][capacity] = max(pick, not_pick)

        return dp_arr[size - 1][size]
