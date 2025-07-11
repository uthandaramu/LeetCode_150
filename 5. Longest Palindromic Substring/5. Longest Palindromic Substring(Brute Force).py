class Solution(object):
    def isPalindrome(self, word):
        return word == word[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1: return s

        result = ""

        #Expand around center
        for center in range(1, size):

            #To find odd palindrome
            i = j = center

            while i >= 0 and j < size:
                newWord = s[i: j + 1]
                if self.isPalindrome(newWord):
                    if len(result) < len(newWord):
                        result = newWord
                    i -= 1
                    j += 1
                else:
                    break

            #To find even palindrome
            i = center - 1
            j = center

            while i >= 0 and j < size:
                newWord = s[i: j + 1]
                if self.isPalindrome(newWord):
                    if len(result) < len(newWord):
                        result = newWord
                    i -= 1
                    j += 1
                else:
                    break

        return (result)