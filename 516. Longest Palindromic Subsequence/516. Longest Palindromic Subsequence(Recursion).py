class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        size = len(s)
        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if s[idx1] == s2[idx2]:
                return 1 + rec_string(idx1-1, idx2-1)
            else:
                return max(rec_string(idx1, idx2-1), rec_string(idx1-1, idx2))
        
        x = rec_string(size-1, size-1)
        return (x)