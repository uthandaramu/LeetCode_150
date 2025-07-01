class Solution(object):
    def sumSquare(self, n):
        result = 0
        while n:
            digit = n % 10
            result += digit ** 2
            n = n // 10
        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        visited = set()

        while n not in visited:

            result = self.sumSquare(n)
            if result == 1:
                return True
            
            visited.add(n)
            n = result
        
        return False