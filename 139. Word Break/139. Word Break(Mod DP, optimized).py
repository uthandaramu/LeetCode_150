class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)
        dp_arr = [False] * (size + 1)

        # Base case : "" empty string can always be created from wordDict
        dp_arr[0] = True

        setDict = set()
        maxLength = 0

        for word in wordDict:
            setDict.add(word)
            maxLength = max(maxLength, len(word))

        for i in range(1, size + 1):
            for j in range(max(0, i - maxLength), i):
                # checks only if previous break is possible
                if dp_arr[j] and s[j: i] in setDict:
                    dp_arr[i] = True
                    break

        return dp_arr[size]