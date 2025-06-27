class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ch_to_word = {}
        word_to_ch = {}

        word_arr = s.split(" ")

        if len(word_arr) != len(pattern):
            return False

        for char, word in zip(pattern, word_arr):
            if char in ch_to_word:
                if ch_to_word[char] != word:
                    return False

            else:
                if word in word_to_ch:
                    return False
                ch_to_word[char] = word
                word_to_ch[word] = char

        return True