class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + (rec_string(idx1 - 1, idx2 - 1))
            else:
                return max(rec_string(idx1 - 1, idx2), rec_string(idx1, idx2 - 1))

        x = rec_string(length1 - 1, length2 - 1)
        return (x)