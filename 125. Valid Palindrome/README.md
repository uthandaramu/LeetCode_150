### 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"  
**Output:** true  
**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**

**Input:** s = "race a car"  
**Output:** false  
**Explanation:** "raceacar" is not a palindrome.

**Example 3:**

**Input:** s = " "  
**Output:** true  
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
**Constraints:**

* 1 <= s.length <= 2 * 105
* s consists only of printable ASCII characters.

### Naive Solution

```python
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
```

### Optimal solution

```python
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
```