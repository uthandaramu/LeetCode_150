from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charFrequency = defaultdict(int)

        for char in t:
            charFrequency[char] += 1

        size = len(s)

        minLength = (10 ** 5) + 1
        startIndex = -1

        left = right = count = 0

        while right < size and left < size:

            # count will be increased if a char was preset using t string
            if charFrequency[s[right]] > 0:
                count += 1
            charFrequency[s[right]] -= 1

            # left pointer will be moved to get minimum possible substring start index
            while left <= right and count == len(t):

                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    startIndex = left
                charFrequency[s[left]] += 1

                if charFrequency[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1

        return "" if startIndex == -1 else s[startIndex:startIndex + minLength]