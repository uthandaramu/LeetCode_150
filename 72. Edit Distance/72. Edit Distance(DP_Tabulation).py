class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        dp_arr = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]

        # Base Case
        for j in range(size2 + 1):
            dp_arr[0][j] = j
        for i in range(size1 + 1):
            dp_arr[i][0] = i

        for idx1 in range(1, size1 + 1):
            for idx2 in range(1, size2 + 1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    dp_arr[idx1][idx2] = 0 + dp_arr[idx1 - 1][idx2 - 1]
                else:
                    dp_arr[idx1][idx2] = min(
                        1 + dp_arr[idx1][idx2 - 1],  # Insert
                        1 + dp_arr[idx1 - 1][idx2],  # Delete
                        1 + dp_arr[idx1 - 1][idx2 - 1]  # Replace
                    )

        return dp_arr[size1][size2]