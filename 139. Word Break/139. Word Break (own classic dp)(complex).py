class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = set()

        size = len(s)

        for word in wordDict:
            word_dict.add(word)

        dp_arr = [[-1 for _ in range(size)] for _ in range(size)]

        def recBreak(left, right):

            if right == size:
                return True if s[left:right] in word_dict else False

            if dp_arr[left][right] == -1:
                if s[left:right] in word_dict:
                    dp_arr[left][right] = recBreak(right, right) or recBreak(left, right + 1)
                else:
                    dp_arr[left][right] = recBreak(left, right + 1)

            return dp_arr[left][right]

        x = recBreak(0, 0)
        return x