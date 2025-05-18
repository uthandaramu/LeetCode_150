class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        dp_arr = [[-1 for _ in range(amount + 1)] for _ in range(size)]

        def rec_change(idx, target):
            if target == 0:
                return 1
            if idx == 0:
                if target >= coins[idx] and target % coins[idx] == 0:
                    return 1
                else:
                    return 0
            if dp_arr[idx][target] == -1:
                not_pick = rec_change(idx - 1, target)
                pick = 0
                if coins[idx] <= target:
                    pick = rec_change(idx, target - coins[idx])
                dp_arr[idx][target] = pick + not_pick
            return dp_arr[idx][target]

        return (rec_change(size - 1, amount))