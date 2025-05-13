### 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<img src="https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png" width = "200">

**Example 1:**

Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Example 2:**

Input: digits = ""  
Output: []

**Example 3:**

Input: digits = "2"  
Output: ["a","b","c"]
 
**Constraints:**

0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

```python
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
```