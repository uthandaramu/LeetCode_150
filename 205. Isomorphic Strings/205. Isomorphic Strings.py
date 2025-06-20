class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_dict = {}

        size = len(s)

        for i in range(size):
            char = s[i]
            if char not in hash_dict:
                if t[i] in hash_dict.values():
                    return False

                hash_dict[char] = t[i]

            elif hash_dict[char] != t[i]:
                return False

        return True