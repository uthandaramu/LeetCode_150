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

        def rec_coin(idx, target):
            if idx == 0:
                if target % coins[idx] == 0:
                    return target / coins[idx]
                else:
                    return 1e9
            if dp_arr[idx][target] == 1e8:
                not_pick = rec_coin(idx - 1, target)
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + rec_coin(idx, target - coins[idx])
                dp_arr[idx][target] = min(pick, not_pick)
            return dp_arr[idx][target]

        x = rec_coin(size - 1, amount)
        return x if x < 1e8 else -1