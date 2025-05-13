### 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**

Input: n = 2  
Output: 2   
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**

Input: n = 3  
Output: 3  
Explanation: There are three ways to climb to the top.  
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

**Constraints:**

1 <= n <= 45 

### With Recursion

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp_rec(n):
            if n == 0:
                return 1
            if n<0:
                return 0
            one_step = dp_rec(n-1)
            two_step = dp_rec(n-2)
            return(one_step+two_step)
        
        return dp_rec(n)
```

### With Dynamic Programming

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_arr = [-1]*n
        def dp_rec(n):
            if n == 0:
                return 1
            if n<0:
                return 0
            if dp_arr[n-1] == -1:
                one_step = dp_rec(n-1)
                two_step = dp_rec(n-2)
            else:
                return dp_arr[n-1]
            dp_arr[n-1] = one_step + two_step
            return(one_step+two_step)
        
        return dp_rec(n)
```

### With Dynamic Programming (Space Optimized)

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
          return 1  
        prev2 = 0
        prev = 1
        res = 0
        for cur in range(n):
            res = prev2 + prev
            prev2 = prev
            prev = res
        return res
```