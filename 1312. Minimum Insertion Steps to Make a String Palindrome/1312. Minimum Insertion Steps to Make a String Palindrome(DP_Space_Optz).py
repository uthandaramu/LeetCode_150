class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        prev_arr = [0 for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            cur_arr = [0 for _ in range(size+1)]
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2-1]
                else:
                    cur_arr[idx2] = max(prev_arr[idx2], cur_arr[idx2-1])
            prev_arr = cur_arr
        
        return (size - prev_arr[size])
