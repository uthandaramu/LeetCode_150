class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        def rec_all_ops(idx1, idx2):
            if idx1 < 0:
                # String 1 Exhausted
                return idx2 + 1
            if idx2 < 0:
                # String 2 Exhausted
                return idx1 + 1
            if word1[idx1] == word2[idx2]:
                return 0 + rec_all_ops(idx1 - 1, idx2 - 1)

            return min(
                1 + rec_all_ops(idx1, idx2 - 1),  # Insert
                1 + rec_all_ops(idx1 - 1, idx2),  # Delete
                1 + rec_all_ops(idx1 - 1, idx2 - 1)
            )

        x = rec_all_ops(size1 - 1, size2 - 1)
        return x