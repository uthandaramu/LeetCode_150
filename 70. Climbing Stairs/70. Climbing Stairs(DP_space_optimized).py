class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
          return 1  
        prev2 = 0
        prev = 1
        res = 0
        for cur in range(n):
            res = prev2 + prev
            prev2 = prev
            prev = res
        return res