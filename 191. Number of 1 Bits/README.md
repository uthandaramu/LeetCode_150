### 191. Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

**Example 1:**

**Input:** n = 11

**Output:** 3

**Explanation:**

The input binary string 1011 has a total of three set bits.

**Example 2:**

**Input:** n = 128

**Output:** 1

**Explanation:**

The input binary string 10000000 has a total of one set bit.

**Example 3:**

**Input:** n = 2147483645

**Output:** 30

**Explanation:**

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

**Constraints:**

* 1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?  

### With built ins

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)
        count = 0
        for bit in binary:
            if bit == "1":
                count += 1
        return count
```

### Proper Approach

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        n & (n-1) runs till number of ones in the n, each time it sets single one to 0
        """
        res = 0
        while n:
            n = n & (n-1)
            res += 1

        return res
```
