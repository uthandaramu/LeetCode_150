from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackSpace = deque()

        bracMatch = {"}": "{", ")": "(", "]":"["}

        for char in s:
            if char in [")", "}", "]"]:
                if not stackSpace or stackSpace.pop() != bracMatch[char]:
                    return False
            else:
                stackSpace.append(char)

        return True if not stackSpace else False