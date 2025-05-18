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
        dp_arr = [[1e8 for _ in range(amount + 1)] for _ in range(size)]

        for any_t in range(amount + 1):
            if any_t % coins[0] == 0:
                dp_arr[0][any_t] = any_t / coins[0]

        for idx in range(1, size):
            for target in range(amount + 1):
                not_pick = dp_arr[idx - 1][target]
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + dp_arr[idx][target - coins[idx]]
                dp_arr[idx][target] = min(pick, not_pick)

        x = dp_arr[size - 1][amount]
        return x if x < 1e8 else -1