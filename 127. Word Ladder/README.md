### 127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

* Every adjacent pair of words differs by a single letter.
* Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
* sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

**Example 1:**

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]  
**Output:** 5  
**Explanation:** One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

**Example 2:**

**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]  
**Output:** 0  
**Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

**Constraints:**

* 1 <= beginWord.length <= 10
* endWord.length == beginWord.length
* 1 <= wordList.length <= 5000
* wordList[i].length == beginWord.length
* beginWord, endWord, and wordList[i] consist of lowercase English letters.
* beginWord != endWord
* All the words in wordList are unique.

### Intuition: Use BFS over DFS as BFS explores shortest path by default but DFS explore the deepest path

```python
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = set(wordList)
        visited = set()
        
        wordQ = deque()
        wordQ.append((beginWord, 1))

        while wordQ:
            word, tranCount = wordQ.popleft()

            if word == endWord:
                return tranCount

            for idx in range(len(word)):
                for char in range(97, 123):
                    newWord = word[:idx] + chr(char) + word[idx+1:]
                    if newWord not in visited and newWord in wordDict:
                        visited.add(newWord)
                        wordQ.append((newWord, tranCount+1))

        return 0
```