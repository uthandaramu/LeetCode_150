### 139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

Input: s = "leetcode", wordDict = ["leet","code"]  
Output: true  
Explanation: Return true because "leetcode" can be segmented as "leet code".

**Example 2:**

Input: s = "applepenapple", wordDict = ["apple","pen"]  
Output: true  
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".  
Note that you are allowed to reuse a dictionary word.

**Example 3:**

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]  
Output: false

**Constraints:**

* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* 1 <= wordDict[i].length <= 20
* s and wordDict[i] consist of only lowercase English letters.
* All the strings of wordDict are unique.

### Own Approach (classic DP and complex)

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = set()

        size = len(s)

        for word in wordDict:
            word_dict.add(word)
        
        dp_arr = [[-1 for _ in range(size)] for _ in range(size)]

        def recBreak(left, right):

            if right == size:
                return True if s[left:right] in word_dict else False
            
            if dp_arr[left][right] == -1:
                if s[left:right] in word_dict:
                    dp_arr[left][right] = recBreak(right, right) or recBreak(left, right+1)
                else:
                    dp_arr[left][right] = recBreak(left, right+1)
                    
            return dp_arr[left][right]
        
        x = recBreak(0, 0)
        return x
```

### Modified Dp with memoization (optimized and simple)

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)
        dp_arr = [False] * (size + 1)

        #Base case : "" empty string can always be created from wordDict
        dp_arr[0] = True

        setDict = set()
        maxLength = 0

        for word in wordDict:
            setDict.add(word)
            maxLength = max(maxLength, len(word))

        for i in range(1, size+1):
            for j in range(max(0, i - maxLength), i):
                #checks only if previous break is possible
                if dp_arr[j] and s[j : i] in setDict:
                    dp_arr[i] = True
                    break
        
        return dp_arr[size]
```