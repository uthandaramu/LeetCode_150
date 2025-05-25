class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        dp_arr = [[0 for _ in range(size+1)] for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1-1][idx2-1]
                else:
                    dp_arr[idx1][idx2] = max(dp_arr[idx1-1][idx2], dp_arr[idx1][idx2-1])
        
        return (size - dp_arr[size][size])
