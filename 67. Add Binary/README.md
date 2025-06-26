
Code
Testcase
Testcase
Test Result
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

**Example 1:**

Input: a = "11", b = "1"  
Output: "100"

**Example 2:**

Input: a = "1010", b = "1011"  
Output: "10101"
 

**Constraints:**

* 1 <= a.length, b.length <= 104
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.

### Own Approach (Without in-built)

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        size1 = len(a)
        size2 = len(b)

        i = size1-1
        j = size2-1

        res = ""

        carry = 0

        while i >= 0 or j >= 0:
            if i < 0 or j < 0:
                if i < 0:
                    char_a = "0"
                    char_b = b[j]
                if j < 0:
                    char_b = "0"
                    char_a = a[i]
            else:
                char_a = a[i]
                char_b = b[j]

            if char_a == char_b:
                add = "0"
                if carry:
                    add = "1"
                    carry = 0
                if char_a == "1":
                    carry = 1
            else:
                add = "1"
                if carry:
                    add = "0"

            res = add + res
            i -= 1
            j -= 1
        
        return ("1" + res) if carry else res
```

### With Inbuilt

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)

        c = bin(a + b)  #bin() returs "0b"+ <eqivalent binary string>

        return c[2:] #Trimming "0b"
```