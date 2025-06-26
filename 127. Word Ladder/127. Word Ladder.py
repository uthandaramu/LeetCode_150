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
                    newWord = word[:idx] + chr(char) + word[idx + 1:]
                    if newWord not in visited and newWord in wordDict:
                        visited.add(newWord)
                        wordQ.append((newWord, tranCount + 1))

        return 0