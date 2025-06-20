class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        vocab_dict = {}
        for char in s:
            if char not in vocab_dict:
                vocab_dict[char] = 1
            else:
                vocab_dict[char] += 1

        for char in t:
            if char not in vocab_dict:
                return False
            else:
                if vocab_dict[char] == 1:
                    vocab_dict.pop(char)
                else:
                    vocab_dict[char] -= 1

        return True if not vocab_dict else False