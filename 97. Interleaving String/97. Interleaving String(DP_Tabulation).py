class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != (len1 + len2): return False

        dp_arr = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1, -1, -1):
            for j in range(len2, -1, -1):

                # base case
                if i == len1 and j == len2:
                    dp_arr[i][j] = True
                    continue

                k = i + j
                dp_arr[i][j] = False
                if i < len1 and s1[i] == s3[k] and dp_arr[i + 1][j]:
                    dp_arr[i][j] = True

                if j < len2 and s2[j] == s3[k] and dp_arr[i][j + 1]:
                    dp_arr[i][j] = True

        return dp_arr[0][0]