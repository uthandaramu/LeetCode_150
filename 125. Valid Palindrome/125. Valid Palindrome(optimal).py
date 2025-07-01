class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        for char in s:
            if char.isalnum():
                result.append(char.lower())
        
        string = "".join(result)

        return string == string[::-1]