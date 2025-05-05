class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        left <<= count
        return (left)

