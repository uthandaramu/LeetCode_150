class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        vocab_dict = {}
        for i in magazine:
            if i in vocab_dict:
                vocab_dict[i] += 1
            else:
                vocab_dict[i] = 1

        for j in ransomNote:
            if j in vocab_dict and vocab_dict[j] > 0:
                vocab_dict[j] -= 1
            else:
                return False
        return True