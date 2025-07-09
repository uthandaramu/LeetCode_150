class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        visited = set()

        size = len(s)
        result = left = right = 0

        while right < size and left <= right:
            if s[right] not in visited:
                result = max(result, (right - left + 1))

            else:
                while left <= right and s[right] in visited:
                    visited.remove(s[left])
                    left += 1

            visited.add(s[right])
            right += 1

        return (result)