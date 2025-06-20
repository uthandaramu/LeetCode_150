### 224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

**Example 1:**

Input: s = "1 + 1"  
Output: 2

**Example 2:**

Input: s = " 2-1 + 2 "  
Output: 3

**Example 3:**

Input: s = "(1+(4+5+2)-3)+(6+8)"  
Output: 23
 

**Constraints:**

* 1 <= s.length <= 3 * 105
* s consists of digits, '+', '-', '(', ')', and ' '.
* s represents a valid expression.
* '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
* '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
* There will be no two consecutive operators in the input.
* Every number and running calculation will fit in a signed 32-bit integer.

```python
from collections import deque

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_val = i = 0
        sign_val = 1
        res = 0
        stack_box = deque()
        size = len(s)

        while i < size:
            if s[i].isdigit():
                while i < size and s[i].isdigit():
                    cur_val = cur_val * 10 + int(s[i])
                    i += 1
                i -= 1

                res += (cur_val * sign_val)
                sign_val = 1
                cur_val = 0

            elif s[i] == "+":
                sign_val = 1
            
            elif s[i] == "-":
                sign_val = -1

            elif s[i] == "(":
                stack_box.append(res)
                stack_box.append(sign_val)
                cur_val = 0
                sign_val = 1
                res = 0         
            
            elif s[i] == ")":
                prev_sign = stack_box.pop()
                prev_res = stack_box.pop()
                res *= prev_sign
                res += prev_res

            i+=1

        return res
```