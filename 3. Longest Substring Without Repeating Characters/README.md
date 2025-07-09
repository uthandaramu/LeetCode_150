### 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

**Example 1:**

**Input:** s = "abcabcbb"  
**Output:** 3  
**Explanation:** The answer is "abc", with the length of 3.

**Example 2:**

**Input:** s = "bbbbb"  
**Output:** 1  
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"  
**Output:** 3  
**Explanation:** The answer is "wke", with the length of 3.  
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        visited = set()

        size = len(s)
        result = left = right = 0
        
        while right < size and left <= right:
            if s[right] not in visited:
                result = max(result, (right-left+1))

            else:
                while left <= right and s[right] in visited:
                    visited.remove(s[left])
                    left += 1

            visited.add(s[right])    
            right += 1
        
        return (result)
```