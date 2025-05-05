from collections import deque

class MinStack(object):

    def __init__(self):
        self.box = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.box) == 0:
            self.box.append((val, val))
        else:
            if self.box[-1][1] > val:
                self.box.append((val, val))
            else:
                self.box.append((val, self.box[-1][1]))

    def pop(self):
        """
        :rtype: None
        """
        self.box.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.box[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.box[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()