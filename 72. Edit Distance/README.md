### 72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character  
Delete a character  
Replace a character  
 

**Example 1:**

Input: word1 = "horse", word2 = "ros"  
Output: 3  
Explanation:   
horse -> rorse (replace 'h' with 'r')  
rorse -> rose (remove 'r')  
rose -> ros (remove 'e')  

**Example 2:**

Input: word1 = "intention", word2 = "execution"  
Output: 5  
Explanation:   
intention -> inention (remove 't')  
inention -> enention (replace 'i' with 'e')  
enention -> exention (replace 'n' with 'x')  
exention -> exection (replace 'n' with 'c')  
exection -> execution (insert 'u')

**Constraints:**

0 <= word1.length, word2.length <= 500  
word1 and word2 consist of lowercase English letters.

### With Recursion (TLE)

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        def rec_all_ops(idx1, idx2):
            if idx1 < 0:
                #String 1 Exhausted
                return idx2 + 1
            if idx2 < 0:
                #String 2 Exhausted
                return idx1 + 1
            if word1[idx1] == word2[idx2]:
                return 0 + rec_all_ops(idx1-1, idx2-1)

            return min(
                1 + rec_all_ops(idx1, idx2-1),          #Insert
                1 + rec_all_ops(idx1-1, idx2),          #Delete
                1 + rec_all_ops(idx1-1, idx2-1)
            )
        
        x = rec_all_ops(size1-1, size2-1)
        return x
```

### With Dynamic Programing

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        dp_arr = [[-1 for _ in range(size2)] for _ in range(size1)]

        def rec_all_ops(idx1, idx2):
            if idx1 < 0:
                #String 1 Exhausted
                return idx2 + 1
            if idx2 < 0:
                #String 2 Exhausted
                return idx1 + 1
            if dp_arr[idx1][idx2] == -1:

                if word1[idx1] == word2[idx2]:
                    res = 0 + rec_all_ops(idx1-1, idx2-1)
                else:
                    res = min(
                        1 + rec_all_ops(idx1, idx2-1),          #Insert
                        1 + rec_all_ops(idx1-1, idx2),          #Delete
                        1 + rec_all_ops(idx1-1, idx2-1)         #Replace
                    )
                dp_arr[idx1][idx2] = res

            return dp_arr[idx1][idx2]
        
        x = rec_all_ops(size1-1, size2-1)
        return x
```

### With Dynamic Programing (Tabulation)

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        dp_arr = [[0 for _ in range(size2+1)] for _ in range(size1+1)]

        #Base Case
        for j in range(size2+1):
            dp_arr[0][j] = j
        for i in range(size1+1):
            dp_arr[i][0] = i

        for idx1 in range(1, size1+1):
            for idx2 in range(1, size2+1):
                if word1[idx1-1] == word2[idx2-1]:
                    dp_arr[idx1][idx2] = 0 + dp_arr[idx1-1][idx2-1]
                else:
                    dp_arr[idx1][idx2] = min(
                        1 + dp_arr[idx1][idx2-1],  #Insert
                        1 + dp_arr[idx1-1][idx2],  #Delete
                        1 + dp_arr[idx1-1][idx2-1]   #Replace
                    )
        
        return dp_arr[size1][size2]
```

### With Dynamic Programing (Space Optimized)

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size1 = len(word1)
        size2 = len(word2)

        prev_arr = [i for i in range(size2+1)]

        for idx1 in range(1, size1+1):
            cur_arr = [0 for _ in range(size2+1)]
            cur_arr[0] = idx1
            for idx2 in range(1, size2+1):
                if word1[idx1-1] == word2[idx2-1]:
                    cur_arr[idx2] = 0 + prev_arr[idx2-1]
                else:
                    cur_arr[idx2] = min(
                        1 + cur_arr[idx2-1],  #Insert
                        1 + prev_arr[idx2],  #Delete
                        1 + prev_arr[idx2-1]   #Replace
                    )
            
            prev_arr = cur_arr
        
        return prev_arr[size2]
```