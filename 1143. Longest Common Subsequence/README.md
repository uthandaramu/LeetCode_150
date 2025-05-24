### 1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.  

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.  

For example, "ace" is a subsequence of "abcde".  
A common subsequence of two strings is a subsequence that is common to both strings.

**Example 1:**

Input: text1 = "abcde", text2 = "ace"   
Output: 3    
Explanation: The longest common subsequence is "ace" and its length is 3.

**Example 2:**

Input: text1 = "abc", text2 = "abc"  
Output: 3  
Explanation: The longest common subsequence is "abc" and its length is 3.

**Example 3:**

Input: text1 = "abc", text2 = "def"  
Output: 0  
Explanation: There is no such common subsequence, so the result is 0.  

**Constraints:**

1 <= text1.length, text2.length <= 1000  
text1 and text2 consist of only lowercase English characters.

### With Recursion

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + (rec_string(idx1 - 1, idx2 - 1))
            else:
                return max(rec_string(idx1 - 1, idx2), rec_string(idx1, idx2 - 1))

        x = rec_string(length1 - 1, length2 - 1)
        return (x)
```

### With Dynamic Programing

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        dp_arr = [[-1 for _ in range(length2)] for _ in range(length1)]
        def rec_string(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if dp_arr[idx1][idx2] == -1:
                if text1[idx1] == text2[idx2]:
                    dp_arr[idx1][idx2] = 1 + (rec_string(idx1-1, idx2-1))
                else:
                    dp_arr[idx1][idx2] = max(rec_string(idx1-1, idx2), rec_string(idx1, idx2-1))
            return dp_arr[idx1][idx2]
        
        x = rec_string(length1-1, length2-1)
        return (x)
```

### Dynamic Programing(bit shifted for proper base case identification)

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        dp_arr = [[-1 for _ in range(length2+1)] for _ in range(length1+1)]
        def rec_string(idx1, idx2):
            if idx1 == 0 or idx2 == 0:
                return 0
            if dp_arr[idx1][idx2] == -1:
                if text1[idx1-1] == text2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + (rec_string(idx1-1, idx2-1))
                else:
                    dp_arr[idx1][idx2] = max(rec_string(idx1-1, idx2), rec_string(idx1, idx2-1))
            return dp_arr[idx1][idx2]
        
        x = rec_string(length1, length2)
        return (x)
```

### Dynamic Programing (With Tabulation)

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        dp_arr = [[0 for _ in range(length2+1)] for _ in range(length1+1)]
        
        for i in range(length1+1):
            dp_arr[i][0] = 0
        for j in range(length2+1):
            dp_arr[0][j] = 0
        
        for idx1 in range(1, length1+1):
            for idx2 in range(1, length2+1):
                if text1[idx1-1] == text2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1-1][idx2-1]
                else:
                    dp_arr[idx1][idx2] = max(dp_arr[idx1-1][idx2], dp_arr[idx1][idx2-1])
        
        return dp_arr[length1][length2]
```

### With Dynamic Programing (Space optimized)

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        length1 = len(text1)
        length2 = len(text2)

        prev_arr = [0 for _ in range(length2+1)] 
        
        """for i in range(length1+1):
            dp_arr[i][0] = 0
        for j in range(length2+1):
            dp_arr[0][j] = 0"""
        
        for idx1 in range(1, length1+1):
            cur_arr = [0 for _ in range(length2+1)]
            for idx2 in range(1, length2+1):
                if text1[idx1-1] == text2[idx2-1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2-1]
                else:
                    cur_arr[idx2] = max(prev_arr[idx2], cur_arr[idx2-1])
            
            prev_arr = cur_arr
        
        return prev_arr[length2]
```