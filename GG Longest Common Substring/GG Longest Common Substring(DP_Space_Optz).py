# User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        length1 = len(s1)
        length2 = len(s2)

        prev_arr = [0 for _ in range(length2 + 1)]

        out = 0

        for idx1 in range(1, length1 + 1):
            cur_arr = [0 for _ in range(length2 + 1)]
            for idx2 in range(1, length2 + 1):
                if s1[idx1 - 1] == s2[idx2 - 1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2 - 1]
                    out = max(out, cur_arr[idx2])
                else:
                    cur_arr[idx2] = 0
            prev_arr = cur_arr

        return out
