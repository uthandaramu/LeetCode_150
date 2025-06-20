class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""

        word = ""

        size = len(s)

        for i in range(size):
            if s[i] != " ":
                word += s[i]
            else:
                if len(word):
                    out = word + " " + out
                    word = ""
                continue

        if len(word):
            out = word + " " + out

        return (out[:-1])