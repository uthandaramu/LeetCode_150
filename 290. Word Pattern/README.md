### 290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.  
Each unique word in s maps to exactly one letter in pattern.  
No two letters map to the same word, and no two words map to the same letter.
 

**Example 1:**

**Input:** pattern = "abba", s = "dog cat cat dog"

**Output:** true

**Explanation:**

The bijection can be established as:

* 'a' maps to "dog".
* 'b' maps to "cat".

**Example 2:**

**Input:** pattern = "abba", s = "dog cat cat fish"

**Output:** false

**Example 3:**

**Input:** pattern = "aaaa", s = "dog cat cat dog"

**Output:** false

**Constraints:**

* 1 <= pattern.length <= 300
* pattern contains only lower-case English letters.
* 1 <= s.length <= 3000
* s contains only lowercase English letters and spaces ' '.
* s does not contain any leading or trailing spaces.
* All the words in s are separated by a single space.

### Own Approach (Space optimized)

```python
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_arr = s.split(" ")
        hash_dict = {}

        if len(word_arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]

            if char not in hash_dict:
                if word_arr[i] not in hash_dict.values():
                    hash_dict[char] = word_arr[i]
                else:
                    return False

            else:
                if hash_dict[char] != word_arr[i]:
                    return False

        return True
```

### Better Readability

```python
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ch_to_word = {}
        word_to_ch = {}

        word_arr = s.split(" ")

        if len(word_arr) != len(pattern):
            return False
        
        for char, word in zip(pattern, word_arr):
            if char in ch_to_word:
                if ch_to_word[char] != word:
                    return False
            
            else:
                if word in word_to_ch:
                    return False
                ch_to_word[char] = word
                word_to_ch[word] = char
        
        return True
```