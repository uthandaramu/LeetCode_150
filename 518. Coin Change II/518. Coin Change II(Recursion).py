class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        def rec_change(idx, target):
            if target == 0:
                return 1
            if idx == 0:
                if target >= coins[idx] and target % coins[idx] == 0:
                    return 1
                else:
                    return 0
            not_pick = rec_change(idx - 1, target)
            pick = 0
            if coins[idx] <= target:
                pick = rec_change(idx, target - coins[idx])
            return pick + not_pick

        return (rec_change(size - 1, amount))
