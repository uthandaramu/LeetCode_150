class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_arr = [-1]*n
        def dp_rec(n):
            if n == 0:
                return 1
            if n<0:
                return 0
            if dp_arr[n-1] == -1:
                one_step = dp_rec(n-1)
                two_step = dp_rec(n-2)
            else:
                return dp_arr[n-1]
            dp_arr[n-1] = one_step + two_step
            return(one_step+two_step)
        
        return dp_rec(n)