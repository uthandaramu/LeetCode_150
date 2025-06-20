class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        i = length - 1
        out = 0

        #Skipping Trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        #counting last word length
        while i >= 0 and s[i] != ' ':
            out += 1
            i -= 1

        return out