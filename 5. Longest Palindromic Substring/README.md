### 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

**Example 1:**

**Input:** s = "babad"  
**Output:** "bab"  
**Explanation:** "aba" is also a valid answer.

**Example 2:**

**Input:** s = "cbbd"  
**Output:** "bb"

**Constraints:**

* 1 <= s.length <= 1000
* s consist of only digits and English letters.

### Brute Force

```python
class Solution(object):
    def isPalindrome(self, word):
        return word == word[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1: return s

        result = ""
        
        #Expand around center
        for center in range(1, size):
            
            #To find odd palindrome
            i = j = center

            while i >= 0 and j < size:
                newWord = s[i: j + 1]
                if self.isPalindrome(newWord):
                    if len(result) < len(newWord):
                        result = newWord
                    i -= 1
                    j += 1
                else:
                    break

            #To find even palindrome
            i = center - 1
            j = center

            while i >= 0 and j < size:
                newWord = s[i: j + 1]
                if self.isPalindrome(newWord):
                    if len(result) < len(newWord):
                        result = newWord
                    i -= 1
                    j += 1
                else:
                    break

        return (result)
```

### Optimized approach

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size < 2:
            return s

        result = ""

        def expandCenter(i, j):
            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i+1 : j]
        
        for center in range(1, size):
            #Odd palindrome
            start = end = center
            newPalindrome = expandCenter(start, end)

            if len(result) < len(newPalindrome):
                result = newPalindrome
            
            #Even palindrome
            start = center - 1
            end = center
            newPalindrome = expandCenter(start, end)

            if len(result) < len(newPalindrome):
                result = newPalindrome

        return result
```