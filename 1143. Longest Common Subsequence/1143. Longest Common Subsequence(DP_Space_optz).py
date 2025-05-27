class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        prev_arr = [0 for _ in range(length2 + 1)]

        """for i in range(length1+1):
            dp_arr[i][0] = 0
        for j in range(length2+1):
            dp_arr[0][j] = 0"""

        for idx1 in range(1, length1 + 1):
            cur_arr = [0 for _ in range(length2 + 1)]
            for idx2 in range(1, length2 + 1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2 - 1]
                else:
                    cur_arr[idx2] = max(prev_arr[idx2], cur_arr[idx2 - 1])

            prev_arr = cur_arr

        return prev_arr[length2]