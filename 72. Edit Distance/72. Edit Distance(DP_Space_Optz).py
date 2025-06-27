class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        prev_arr = [i for i in range(size2 + 1)]

        for idx1 in range(1, size1 + 1):
            cur_arr = [0 for _ in range(size2 + 1)]
            cur_arr[0] = idx1
            for idx2 in range(1, size2 + 1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    cur_arr[idx2] = 0 + prev_arr[idx2 - 1]
                else:
                    cur_arr[idx2] = min(
                        1 + cur_arr[idx2 - 1],  # Insert
                        1 + prev_arr[idx2],  # Delete
                        1 + prev_arr[idx2 - 1]  # Replace
                    )

            prev_arr = cur_arr

        return prev_arr[size2]