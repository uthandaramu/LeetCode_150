class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        dp_arr = [[0 for _ in range(amount + 1)] for _ in range(size)]

        for i in range(size):
            dp_arr[i][0] = 1
        for i in range(amount + 1):
            if i >= coins[0] and i % coins[0] == 0:
                dp_arr[0][i] = 1
        for idx in range(1, size):
            for target in range(amount + 1):
                not_pick = dp_arr[idx - 1][target]
                pick = 0
                if coins[idx] <= target:
                    pick = dp_arr[idx][target - coins[idx]]
                dp_arr[idx][target] = pick + not_pick

        return dp_arr[size - 1][amount]
