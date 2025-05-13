class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp_rec(n):
            if n == 0:
                return 1
            if n<0:
                return 0
            one_step = dp_rec(n-1)
            two_step = dp_rec(n-2)
            return(one_step+two_step)
        
        return dp_rec(n)