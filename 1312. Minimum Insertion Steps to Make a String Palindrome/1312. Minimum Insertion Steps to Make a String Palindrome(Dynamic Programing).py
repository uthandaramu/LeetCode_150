class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        dp_arr = [[-1 for _ in range(size)] for _ in range(size)]
        def rec_insert(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if dp_arr[idx1][idx2] == -1:
                if s[idx1] == s2[idx2]:
                    dp_arr[idx1][idx2] = (1 + rec_insert(idx1-1, idx2-1))
                else:
                    dp_arr[idx1][idx2] = max(rec_insert(idx1, idx2-1), rec_insert(idx1-1, idx2))
            
            return dp_arr[idx1][idx2]

        x = rec_insert(size-1, size-1)
        return (size - x)
        