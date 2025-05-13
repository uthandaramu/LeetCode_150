class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        out_arr = []
        word_size = len(digits)
        if word_size==0:
            return out_arr
        phone_dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        def backtrack(digit, curStr):
            if len(curStr) == len(digits):
                out_arr.append(curStr)
                return
            for letter in phone_dict[digits[digit]]:
                backtrack(digit+1, curStr+letter)
        
        if digits:
            backtrack(0, "")

        return out_arr