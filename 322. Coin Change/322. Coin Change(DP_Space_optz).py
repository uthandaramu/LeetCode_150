class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return amount
        size = len(coins)
        prev_arr = [1e8 for _ in range(amount + 1)]

        for any_t in range(amount + 1):
            if any_t % coins[0] == 0:
                prev_arr[any_t] = any_t / coins[0]

        for idx in range(1, size):
            cur_arr = [1e8 for _ in range(amount + 1)]
            for target in range(amount + 1):
                not_pick = prev_arr[target]
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + cur_arr[target - coins[idx]]
                cur_arr[target] = min(pick, not_pick)
            prev_arr = cur_arr

        x = prev_arr[amount]
        return x if x < 1e8 else -1