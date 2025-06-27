class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        n & (n-1) runs till number of ones in the n, each time it sets single one to 0
        """
        res = 0
        while n:
            n = n & (n-1)
            res += 1

        return res