class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                idx = magazine.find(i)
                magazine = magazine[:idx] + magazine[idx+1:]
            else:
                return False
        return True