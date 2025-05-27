class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        prev_arr = [0 for _ in range(amount + 1)]

        prev_arr[0] = 1
        for i in range(amount + 1):
            if i >= coins[0] and i % coins[0] == 0:
                prev_arr[i] = 1
        for idx in range(1, size):
            cur_arr = [0 for _ in range(amount + 1)]
            for target in range(amount + 1):
                not_pick = prev_arr[target]
                pick = 0
                if coins[idx] <= target:
                    pick = cur_arr[target - coins[idx]]
                cur_arr[target] = pick + not_pick
            prev_arr = cur_arr

        return prev_arr[amount]