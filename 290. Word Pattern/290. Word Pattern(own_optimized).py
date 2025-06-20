class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_arr = s.split(" ")
        hash_dict = {}

        if len(word_arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]

            if char not in hash_dict:
                if word_arr[i] not in hash_dict.values():
                    hash_dict[char] = word_arr[i]
                else:
                    return False

            else:
                if hash_dict[char] != word_arr[i]:
                    return False

        return True