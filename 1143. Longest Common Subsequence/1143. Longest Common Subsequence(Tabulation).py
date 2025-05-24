class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        dp_arr = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]

        for i in range(length1 + 1):
            dp_arr[i][0] = 0
        for j in range(length2 + 1):
            dp_arr[0][j] = 0

        for idx1 in range(1, length1 + 1):
            for idx2 in range(1, length2 + 1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1 - 1][idx2 - 1]
                else:
                    dp_arr[idx1][idx2] = max(dp_arr[idx1 - 1][idx2], dp_arr[idx1][idx2 - 1])

        return dp_arr[length1][length2]