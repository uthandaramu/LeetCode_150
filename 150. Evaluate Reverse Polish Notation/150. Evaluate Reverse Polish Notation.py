from collections import deque

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stackPolish = deque()

        for char in tokens:

            if char == "+":
                stackPolish.append(stackPolish.pop() + stackPolish.pop())

            elif char == "-":
                a, b = stackPolish.pop(), stackPolish.pop()
                stackPolish.append(b - a)

            elif char == "*":
                stackPolish.append(stackPolish.pop() * stackPolish.pop())

            elif char == "/":
                
                a, b = stackPolish.pop(), stackPolish.pop()
                result = int(b / a) if b * a >= 0 else -(-b // a)
                stackPolish.append(result)

                #Note: -5 // 2   == -3 (towards -inf) 
                #Note: int(-5 / 2) == -2 (towards 0)

            else:
                stackPolish.append(int(char))
                #print(stackPolish)
                
        print(int(6/-132))
        return stackPolish.pop()