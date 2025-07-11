### 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
**Example 1:**

**Input:** s = "PAYPALISHIRING", numRows = 3  
**Output:** "PAHNAPLSIIGYIR"

**Example 2:**

**Input:** s = "PAYPALISHIRING", numRows = 4  
**Output:** "PINALSIGYAHRPI" 
 
**Explanation:**  
```
P     I    N  
A   L S  I G  
Y A   H R  
P     I  
```

**Example 3:**

**Input:** s = "A", numRows = 1  
**Output:** "A"
 

**Constraints:**

* 1 <= s.length <= 1000
* s consists of English letters (lower-case and upper-case), ',' and '.'.
* 1 <= numRows <= 1000

```python
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
```