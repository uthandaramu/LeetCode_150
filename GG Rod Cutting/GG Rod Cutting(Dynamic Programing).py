# User function Template for python3

class Solution:
    def cutRod(self, price):
        # code here

        size = len(price)

        dp_arr = [[-1 for _ in range(size + 1)] for _ in range(size)]

        def rec_cut(idx, capacity):
            if idx == 0:
                if capacity >= 1:
                    return capacity * price[idx]
                else:
                    return 0
            if dp_arr[idx][capacity] == -1:
                not_pick = rec_cut(idx - 1, capacity)
                pick = 0
                if capacity >= idx + 1:
                    pick = price[idx] + rec_cut(idx, (capacity - (idx + 1)))
                dp_arr[idx][capacity] = max(pick, not_pick)
            return dp_arr[idx][capacity]

        x = rec_cut(size - 1, size)
        return x