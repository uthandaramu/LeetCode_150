class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size < 2:
            return s

        result = ""

        def expandCenter(i, j):
            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i + 1: j]

        for center in range(1, size):
            # Odd palindrome
            start = end = center
            newPalindrome = expandCenter(start, end)

            if len(result) < len(newPalindrome):
                result = newPalindrome

            # Even palindrome
            start = center - 1
            end = center
            newPalindrome = expandCenter(start, end)

            if len(result) < len(newPalindrome):
                result = newPalindrome

        return result