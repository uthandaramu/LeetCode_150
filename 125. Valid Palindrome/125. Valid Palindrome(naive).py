class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_low = s.lower()
        string = ""
        for char in s_low:
            if char.isalpha() or char.isdigit():
                string += char
        
        print(string)
        if string == string[::-1]:
            return True

        return False