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

        dp_arr = [[-1 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        def recInterleave(i1, i2):
            i3 = i1 + i2
            if i1 == len1 and i2 == len2:
                return True

            if dp_arr[i1][i2] == -1:
                dp_arr[i1][i2] = False

                if i1 < len1 and s1[i1] == s3[i3] and recInterleave(i1 + 1, i2):
                    dp_arr[i1][i2] = True
                if i2 < len2 and s2[i2] == s3[i3] and recInterleave(i1, i2 + 1):
                    dp_arr[i1][i2] = True

            return dp_arr[i1][i2]

        x = recInterleave(0, 0)
        return x