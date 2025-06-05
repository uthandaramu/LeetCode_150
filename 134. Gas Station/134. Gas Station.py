class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        size = len(gas)
        ans = diff = 0
        for i in range(size):
            diff += gas[i] - cost[i]
            if diff < 0:
                ans = i + 1
                diff = 0
        return ans