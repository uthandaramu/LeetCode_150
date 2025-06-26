class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Intuation: 2^10 is 2^5 * 2^5

        def recPow(base, power):
            if base == 0:
                return 0
            if power == 0:
                return 1

            res = recPow(base, power // 2)
            res = res * res
            return base * res if power % 2 else res

        out = recPow(x, abs(n))

        return out if n >= 0 else 1 / (out)