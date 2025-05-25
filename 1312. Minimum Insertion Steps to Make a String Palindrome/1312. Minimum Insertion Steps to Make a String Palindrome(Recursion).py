class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        def rec_insert(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if s[idx1] == s2[idx2]:
                return (1 + rec_insert(idx1-1, idx2-1))
            else:
                return max(rec_insert(idx1, idx2-1), rec_insert(idx1-1, idx2))

        x = rec_insert(size-1, size-1)
        return (size - x)