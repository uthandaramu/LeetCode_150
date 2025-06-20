class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_arr = s.strip().split()

        out = " ".join(reversed(word_arr))

        return out