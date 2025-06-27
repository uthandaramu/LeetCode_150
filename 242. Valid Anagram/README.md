### 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

**Example 1:**

Input: s = "anagram", t = "nagaram"

Output: true

**Example 2:**

Input: s = "rat", t = "car"

Output: false

**Constraints:**

* 1 <= s.length, t.length <= 5 * 104
* s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        vocab_dict = {}
        for char in s:
            if char not in vocab_dict:
                vocab_dict[char] = 1
            else:
                vocab_dict[char] += 1
        
        for char in t:
            if char not in vocab_dict:
                return False
            else:
                if vocab_dict[char] == 1:
                    vocab_dict.pop(char)
                else:
                    vocab_dict[char] -= 1
        
        return True if not vocab_dict else False
```