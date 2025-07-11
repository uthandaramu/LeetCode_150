### 97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn  
t = t1 + t2 + ... + tm  
|n - m| <= 1  
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...  
Note: a + b is the concatenation of strings a and b.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" width="400">

**Input:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"  
**Output:** true  
**Explanation:** One way to obtain s3 is:  
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".  
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".  
Since s3 can be obtained by interleaving s1 and s2, we return true.

**Example 2:**

**Input:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"  
**Output:** false  
**Explanation:** Notice how it is impossible to interleave s2 with any other string to obtain s3.

**Example 3:**

**Input:** s1 = "", s2 = "", s3 = ""  
**Output:** true

**Constraints:**

* 0 <= s1.length, s2.length <= 100
* 0 <= s3.length <= 200
* s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

### With Recursion

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != (len1 + len2): return False

        def recInterleave(i1, i2):
            i3 = i1 + i2
            if i1 == len1 and i2 == len2:
                return True

            if i1 < len1 and s1[i1] == s3[i3] and recInterleave(i1+1, i2):
                return True
            if i2 < len2 and s2[i2] == s3[i3] and recInterleave(i1, i2+1):
                return True

            return False
        
        x = recInterleave(0,0)
        return (x)
```

### With memoization

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != (len1 + len2): return False

        dp_arr = [[-1 for _ in range(len2+1)] for _ in range(len1+1)]

        def recInterleave(i1, i2):
            i3 = i1 + i2
            if i1 == len1 and i2 == len2:
                return True

            if dp_arr[i1][i2] == -1:
                dp_arr[i1][i2] = False

                if i1 < len1 and s1[i1] == s3[i3] and recInterleave(i1+1, i2):
                    dp_arr[i1][i2] = True
                if i2 < len2 and s2[i2] == s3[i3] and recInterleave(i1, i2+1):
                    dp_arr[i1][i2] = True

            return dp_arr[i1][i2]
        
        x = recInterleave(0,0)
        return x
```

### With Dynamic Programming (Tabulation)

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != (len1 + len2): return False

        dp_arr = [[False for _ in range(len2+1)] for _ in range(len1+1)]

        for i in range(len1, -1, -1):
            for j in range(len2, -1, -1):

                #base case
                if i == len1 and j == len2:
                    dp_arr[i][j] = True
                    continue
                
                k = i+j
                dp_arr[i][j] = False
                if i < len1 and s1[i] == s3[k] and dp_arr[i+1][j]:
                    dp_arr[i][j] = True
                
                if j < len2 and s2[j] == s3[k] and dp_arr[i][j+1]:
                    dp_arr[i][j] = True

        return dp_arr[0][0]
```