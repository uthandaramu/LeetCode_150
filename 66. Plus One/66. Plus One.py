class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        carry = 1
        i = size - 1

        while i >= 0 and carry:
            carry = 0
            nextVal = digits[i] + 1 + carry
            carry = nextVal // 10
            nextVal = nextVal % 10
            digits[i] = nextVal
            i -= 1

        if carry:
            digits = [1] + digits[:]

        return digits