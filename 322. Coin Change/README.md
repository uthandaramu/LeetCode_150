### 322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

Input: coins = [1,2,5], amount = 11  
Output: 3  
Explanation: 11 = 5 + 5 + 1

**Example 2:**

Input: coins = [2], amount = 3  
Output: -1  

**Example 3:**

Input: coins = [1], amount = 0  
Output: 0  

**Constraints:**

1 <= coins.length <= 12  
1 <= coins[i] <= 231 - 1  
0 <= amount <= 104  

### With Dynamic Programing

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return amount
        size = len(coins)
        dp_arr = [[1e8 for _ in range(amount+1)] for _ in range(size)]
        def rec_coin(idx, target):
            if idx == 0:
                if target % coins[idx] == 0:
                    return target/coins[idx]
                else:
                    return 1e9
            if dp_arr[idx][target] == 1e8:
                not_pick = rec_coin(idx-1, target)
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + rec_coin(idx, target-coins[idx])
                dp_arr[idx][target] = min(pick, not_pick)
            return dp_arr[idx][target]

        x = rec_coin(size-1, amount)
        return x if x < 1e8 else -1

```

### With Dynamic Programing(Tabulation)

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return amount
        size = len(coins)
        dp_arr = [[1e8 for _ in range(amount+1)] for _ in range(size)]
        
        for any_t in range(amount+1):
            if any_t % coins[0] == 0:
                dp_arr[0][any_t] = any_t/coins[0]
        
        for idx in range(1, size):
            for target in range(amount+1):
                not_pick = dp_arr[idx-1][target]
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + dp_arr[idx][target-coins[idx]]
                dp_arr[idx][target] = min(pick, not_pick)
        
        x = dp_arr[size-1][amount]
        return x if x < 1e8 else -1
```

### With Dynamic Programing(Space Optimized)

```python
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return amount
        size = len(coins)
        prev_arr = [1e8 for _ in range(amount+1)]
        
        for any_t in range(amount+1):
            if any_t % coins[0] == 0:
                prev_arr[any_t] = any_t/coins[0]
        
        for idx in range(1, size):
            cur_arr = [1e8 for _ in range(amount+1)]
            for target in range(amount+1):
                not_pick = prev_arr[target]
                pick = 1e8
                if coins[idx] <= target:
                    pick = 1 + cur_arr[target-coins[idx]]
                cur_arr[target] = min(pick, not_pick)
            prev_arr = cur_arr
        
        x = prev_arr[amount]
        return x if x < 1e8 else -1
```