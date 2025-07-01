class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)

        if size == 1:
            return s

        #interval should not be zero
        interval = max(1, (numRows - 1) * 2)
        result = []

        for row in range(numRows):

            for i in range(row, size, interval):
                result.append(s[i])

                if row > 0 and row < numRows-1:
                    if i + interval - (2*row) < size:
                        result.append(s[i + interval - (2*row)])
        
        return "".join(result)