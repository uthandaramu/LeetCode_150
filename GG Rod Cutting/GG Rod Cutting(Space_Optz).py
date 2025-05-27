# User function Template for python3

class Solution:
    def cutRod(self, price):
        # code here

        size = len(price)

        prev_arr = [0 for _ in range(size + 1)]

        for cap in range(size + 1):
            prev_arr[cap] = (cap) * price[0]

        for idx in range(1, size):
            cur_arr = [0 for _ in range(size + 1)]
            for capacity in range(size + 1):
                not_pick = prev_arr[capacity]
                pick = 0
                if capacity >= idx + 1:
                    pick = price[idx] + cur_arr[capacity - (idx + 1)]
                cur_arr[capacity] = max(pick, not_pick)
            prev_arr = cur_arr

        return prev_arr[size]