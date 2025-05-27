### Longest Common Substring

You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings.

**Examples:**

Input: s1 = "ABCDGH", s2 = "ACDGHR"  
Output: 4  
Explanation: The longest common substring is "CDGH" with a length of 4.  

Input: s1 = "abc", s2 = "acb"  
Output: 1  
Explanation: The longest common substrings are "a", "b", "c" all having length 1.

Input: s1 = "YZ", s2 = "yz"  
Output: 0  

**Constraints:**

1 <= s1.size(), s2.size() <= 103  
Both strings may contain upper and lower case alphabets.  

### With Tabulation

```python
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        length1 = len(s1)
        length2 = len(s2)
        
        dp_arr = [[0 for _ in range(length2+1)] for _ in range(length1+1)]
        
        out = 0
        
        for idx1 in range(1, length1+1):
            for idx2 in range(1, length2+1):
                if s1[idx1-1] == s2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1-1][idx2-1]
                    out = max(out, dp_arr[idx1][idx2])
                else:
                    dp_arr[idx1][idx2] = 0
        
        return out
            
```

### With Dynamic Programing(Space Optimized)

```python
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        length1 = len(s1)
        length2 = len(s2)
        
        prev_arr = [0 for _ in range(length2+1)]
        
        out = 0
        
        for idx1 in range(1, length1+1):
            cur_arr = [0 for _ in range(length2+1)]
            for idx2 in range(1, length2+1):
                if s1[idx1-1] == s2[idx2-1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2-1]
                    out = max(out, cur_arr[idx2])
                else:
                    cur_arr[idx2] = 0
            prev_arr = cur_arr
            
        return out
            
```