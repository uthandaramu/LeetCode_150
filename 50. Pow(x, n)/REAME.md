### 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

**Example 1:**

Input: x = 2.00000, n = 10  
Output: 1024.00000

**Example 2:**

Input: x = 2.10000, n = 3  
Output: 9.26100

**Example 3:**

Input: x = 2.00000, n = -2  
Output: 0.25000  
Explanation: 2-2 = 1/22 = 1/4 = 0.25

**Constraints:**

* -100.0 < x < 100.0
* -231 <= n <= 231-1
* n is an integer.
* Either x is not zero or n > 0.
* -104 <= xn <= 104


```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        #Intuation: 2^10 is 2^5 * 2^5

        def recPow(base, power):
            if base == 0:
                return 0
            if power == 0:
                return 1

            res = recPow(base, power//2)
            res = res * res
            return base * res if power % 2 else res
        
        out = recPow(x, abs(n))

        return out if n >= 0 else 1 / (out)  
```