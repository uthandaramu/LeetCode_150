### 518. Coin Change II

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.  

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.  

You may assume that you have an infinite number of each kind of coin.  

The answer is guaranteed to fit into a signed 32-bit integer.

**Example 1:**

Input: amount = 5, coins = [1,2,5]  
Output: 4  
Explanation: there are four ways to make up the amount:  
5=5  
5=2+2+1  
5=2+1+1+1  
5=1+1+1+1+1  

**Example 2:**

Input: amount = 3, coins = [2]  
Output: 0  
Explanation: the amount of 3 cannot be made up just with coins of 2.

**Example 3:**

Input: amount = 10, coins = [10]  
Output: 1

**Constraints:**

1 <= coins.length <= 300  
1 <= coins[i] <= 5000  
All the values of coins are unique.  
0 <= amount <= 5000

### With Recursion

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)
        def rec_change(idx, target):
            if target == 0:
                return 1
            if idx == 0:
                if target >= coins[idx] and target % coins[idx] == 0:
                    return 1
                else:
                    return 0
            not_pick = rec_change(idx-1, target)
            pick = 0
            if coins[idx] <= target:
                pick = rec_change(idx, target-coins[idx])
            return pick + not_pick
        
        return (rec_change(size-1, amount))
```

### With Dynamic Programing

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        dp_arr = [[-1 for _ in range(amount+1)] for _ in range(size)]

        def rec_change(idx, target):
            if target == 0:
                return 1
            if idx == 0:
                if target >= coins[idx] and target % coins[idx] == 0:
                    return 1
                else:
                    return 0
            if dp_arr[idx][target] == -1:
                not_pick = rec_change(idx-1, target)
                pick = 0
                if coins[idx] <= target:
                    pick = rec_change(idx, target-coins[idx])
                dp_arr[idx][target] = pick + not_pick
            return dp_arr[idx][target]
        
        return (rec_change(size-1, amount))        
```

### With Tabulation

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        dp_arr = [[0 for _ in range(amount+1)] for _ in range(size)] 

        for i in range(size):
            dp_arr[i][0] = 1
        for i in range(amount+1):
            if i >= coins[0] and i % coins[0] == 0:
                dp_arr[0][i] = 1
        for idx in range(1, size):
            for target in range(amount+1):
                not_pick = dp_arr[idx-1][target]
                pick = 0
                if coins[idx] <= target:
                    pick = dp_arr[idx][target-coins[idx]]
                dp_arr[idx][target] = pick + not_pick
        
        return dp_arr[size-1][amount]
```

### With Dynamic Programing(Space optimized)

```python
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)

        prev_arr = [0 for _ in range(amount+1)] 

        prev_arr[0] = 1
        for i in range(amount+1):
            if i >= coins[0] and i % coins[0] == 0:
                prev_arr[i] = 1
        for idx in range(1, size):
            cur_arr = [0 for _ in range(amount+1)]
            for target in range(amount+1):
                not_pick = prev_arr[target]
                pick = 0
                if coins[idx] <= target:
                    pick = cur_arr[target-coins[idx]]
                cur_arr[target] = pick + not_pick
            prev_arr = cur_arr
        
        return prev_arr[amount]
```
