### 76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

**Example 1:**

**Input:** s = "ADOBECODEBANC", t = "ABC"  
**Output:** "BANC"  
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**

**Input:** s = "a", t = "a"  
**Output:** "a"  
**Explanation:** The entire string s is the minimum window.

**Example 3:**

**Input:** s = "a", t = "aa"  
**Output:** ""  
**Explanation:** Both 'a's from t must be included in the window.  
Since the largest window of s only has one 'a', return empty string.

**Constraints:**

* m == s.length
* n == t.length
* 1 <= m, n <= 105
* s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

```python
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charFrequency = defaultdict(int)

        for char in t:
            charFrequency[char] += 1

        size = len(s)

        minLength = (10 ** 5) + 1
        startIndex = -1

        left = right = count = 0

        while right < size and left < size:
            
            #count will be increased if a char was preset using t string
            if charFrequency[s[right]] > 0:
                count += 1
            charFrequency[s[right]] -= 1
            
            #left pointer will be moved to get minimum possible substring start index
            while left <= right and count == len(t):

                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    startIndex = left
                charFrequency[s[left]] += 1

                if charFrequency[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1

        return "" if startIndex == -1 else s[startIndex:startIndex+minLength]
```