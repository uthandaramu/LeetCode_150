### 516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

Input: s = "bbbab"  
Output: 4   
Explanation: One possible longest palindromic subsequence is "bbbb".

**Example 2:**

Input: s = "cbbd"  
Output: 2   
Explanation: One possible longest palindromic subsequence is "bb".
 

**Constraints:**

1 <= s.length <= 1000  
s consists only of lowercase English letters.

### With Recursion

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        size = len(s)
        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if s[idx1] == s2[idx2]:
                return 1 + rec_string(idx1-1, idx2-1)
            else:
                return max(rec_string(idx1, idx2-1), rec_string(idx1-1, idx2))
        
        x = rec_string(size-1, size-1)
        return (x)     
```

### With Dynamic Programing

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        size = len(s)
        dp_arr = [[-1 for _ in range(size)] for _ in range(size)]
        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if dp_arr[idx1][idx2] == -1:
                if s[idx1] == s2[idx2]:
                    dp_arr[idx1][idx2] = 1 + rec_string(idx1-1, idx2-1)
                else:
                    dp_arr[idx1][idx2] = max(rec_string(idx1, idx2-1), rec_string(idx1-1, idx2))
            return dp_arr[idx1][idx2]
        
        x = rec_string(size-1, size-1)
        return (x)     
```

### With Dynamic Programing (Tabulation)

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        size = len(s)
        dp_arr = [[0 for _ in range(size+1)] for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1-1][idx2-1]
                else:
                    dp_arr[idx1][idx2] = max(dp_arr[idx1-1][idx2], dp_arr[idx1][idx2-1])
        
        return dp_arr[size][size]
```

### With Dynamic Programing(Space Optimized)

```python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = s[::-1]
        size = len(s)
        prev_arr = [0 for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            cur_arr = [0 for _ in range(size+1)]
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2-1]
                else:
                    cur_arr[idx2] = max(prev_arr[idx2], cur_arr[idx2-1])
            prev_arr = cur_arr
            
        return prev_arr[size]
```