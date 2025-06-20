### 227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

**Example 1:**

Input: s = "3+2*2"  
Output: 7

**Example 2:**

Input: s = " 3/2 "  
Output: 1

**Example 3:**

Input: s = " 3+5 / 2 "  
Output: 5
 

**Constraints:**

* 1 <= s.length <= 3 * 105
* s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
* s represents a valid expression.
* All the integers in the expression are non-negative integers in the range [0, 231 - 1].
* The answer is guaranteed to fit in a 32-bit integer.

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        i = 0
        res = cur_val = prev_val = 0
        cur_operator = "+"

        while i < size:

            if s[i].isdigit():
                while i < size and s[i].isdigit():
                    cur_val = cur_val * 10 + int(s[i])
                    i += 1
                
                i -= 1

                if cur_operator == "+":
                    res += cur_val
                    prev_val = cur_val
                
                elif cur_operator == "-":
                    res -= cur_val
                    prev_val = -cur_val
                
                elif cur_operator == "*":
                    res -= prev_val
                    prev_val = cur_val * prev_val
                    res += prev_val                

                else:
                    res -= prev_val
                    prev_val = int(float(prev_val)/cur_val)
                    res += prev_val

                cur_val = 0         

            elif s[i] != " ":
                cur_operator = s[i]
            
            i += 1
        
        return res
```