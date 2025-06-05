class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = ans = 0
        end = x
        while start <= end:
            mid = (start + end) // 2
            if (mid * mid) > x:
                end = mid - 1
            elif (mid * mid) <= x:
                ans = mid
                start = mid + 1

        return ans