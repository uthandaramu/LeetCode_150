class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        # find the close 10 powers: 100 for 121, 1000 for 1241
        divVal = 1
        while x >= divVal * 10:
            divVal *= 10

        while x:
            left = x // divVal
            right = x % 10

            if left != right:
                return False

            # chop left digit
            x = x % divVal
            # chop right digit
            x = x // 10

            # since we removed two digits, we need to remove two zeroes from divVal
            divVal = divVal / 100

        return True