### 1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

***Example 1:***

Input: s = "zzazz"  
Output: 0  
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

***Example 2:***

Input: s = "mbadm"  
Output: 2  
Explanation: String can be "mbdadbm" or "mdbabdm".

***Example 3:***

Input: s = "leetcode"  
Output: 5  
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

***Constraints:***

1 <= s.length <= 500  
s consists of lowercase English letters.

### With Recursion

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        def rec_insert(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if s[idx1] == s2[idx2]:
                return (1 + rec_insert(idx1-1, idx2-1))
            else:
                return max(rec_insert(idx1, idx2-1), rec_insert(idx1-1, idx2))

        x = rec_insert(size-1, size-1)
        return (size - x)
```

### With Dynamic Programing

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        dp_arr = [[-1 for _ in range(size)] for _ in range(size)]
        def rec_insert(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if dp_arr[idx1][idx2] == -1:
                if s[idx1] == s2[idx2]:
                    dp_arr[idx1][idx2] = (1 + rec_insert(idx1-1, idx2-1))
                else:
                    dp_arr[idx1][idx2] = max(rec_insert(idx1, idx2-1), rec_insert(idx1-1, idx2))
            
            return dp_arr[idx1][idx2]

        x = rec_insert(size-1, size-1)
        return (size - x)
```

### With Dynamic Programimg(Tabulation)

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        dp_arr = [[0 for _ in range(size+1)] for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    dp_arr[idx1][idx2] = 1 + dp_arr[idx1-1][idx2-1]
                else:
                    dp_arr[idx1][idx2] = max(dp_arr[idx1-1][idx2], dp_arr[idx1][idx2-1])
        
        return (size - dp_arr[size][size])

```

### With Dynamic programing(Space Optimized)

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        s2 = s[::-1]
        prev_arr = [0 for _ in range(size+1)]
        
        for idx1 in range(1, size+1):
            cur_arr = [0 for _ in range(size+1)]
            for idx2 in range(1, size+1):
                if s[idx1-1] == s2[idx2-1]:
                    cur_arr[idx2] = 1 + prev_arr[idx2-1]
                else:
                    cur_arr[idx2] = max(prev_arr[idx2], cur_arr[idx2-1])
            prev_arr = cur_arr
        
        return (size - prev_arr[size])

```