### 9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

**Example 1:**

**Input:** x = 121  
**Output:** true  
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121  
**Output:** false  
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** x = 10  
**Output:** false  
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

**Constraints:**

* -231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        #find the close 10 powers: 100 for 121, 1000 for 1241
        divVal = 1
        while x >= divVal * 10:
            divVal *= 10
        
        while x:
            left = x // divVal
            right = x % 10

            if left != right:
                return False
            
            #chop left digit
            x = x % divVal
            #chop right digit
            x = x // 10

            #since we removed two digits, we need to remove two zeroes from divVal
            divVal = divVal / 100
        
        return True
```