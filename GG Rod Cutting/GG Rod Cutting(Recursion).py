# User function Template for python3

class Solution:
    def cutRod(self, price):
        # code here

        size = len(price)

        def rec_cut(idx, capacity):
            if idx == 0:
                if capacity >= 1:
                    return capacity * price[idx]
                else:
                    return 0
            not_pick = rec_cut(idx - 1, capacity)
            pick = 0
            if capacity >= idx + 1:
                pick = price[idx] + rec_cut(idx, (capacity - (idx + 1)))

            return max(pick, not_pick)

        x = rec_cut(size - 1, size)
        return x