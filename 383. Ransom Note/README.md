### 383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.  

Each letter in magazine can only be used once in ransomNote.  

**Example 1:**

Input: ransomNote = "a", magazine = "b"  
Output: false  

**Example 2:**

Input: ransomNote = "aa", magazine = "ab"  
Output: false  

**Example 3:**

Input: ransomNote = "aa", magazine = "aab"  
Output: true  

**Constraints:**

1 <= ransomNote.length, magazine.length <= 105  
ransomNote and magazine consist of lowercase English letters.  

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        vocab_dict = {}
        for i in magazine:
            if i in vocab_dict:
                vocab_dict[i] += 1
            else:
                vocab_dict[i] = 1
            
        for j in ransomNote:
            if j in vocab_dict and vocab_dict[j] > 0:
                vocab_dict[j] -= 1
            else:
                return False
        return True
```