### 123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**

Input: prices = [3,3,5,0,0,3,1,4]  
Output: 6  
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

**Example 2:**

Input: prices = [1,2,3,4,5]  
Output: 4  
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

**Example 3:**

Input: prices = [7,6,4,3,1]  
Output: 0  
Explanation: In this case, no transaction is done, i.e. max profit = 0.

**Constraints:**

1 <= prices.length <= 105  
0 <= prices[i] <= 105

### With Recursion

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        def rec_trade(idx, buy_flag, cap):
            if idx == size or cap == 0:
                return 0
            if buy_flag:
                profit = max(-prices[idx] + rec_trade(idx+1, 0, cap) , rec_trade(idx+1, 1, cap))
            else:
                profit = max(prices[idx] + rec_trade(idx+1, 1, cap-1) , rec_trade(idx+1, 0, cap))

            return profit
        
        x = rec_trade(0, 1, 2)
        return x
```

### With Dynamic Programing

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(size)]

        def rec_trade(idx, buy_flag, cap):
            if idx == size or cap == 0:
                return 0
            if dp_arr[idx][buy_flag][cap] == -1:
                
                if buy_flag:
                    profit = max(-prices[idx] + rec_trade(idx+1, 0, cap) , rec_trade(idx+1, 1, cap))
                else:
                    profit = max(prices[idx] + rec_trade(idx+1, 1, cap-1) , rec_trade(idx+1, 0, cap))

                dp_arr[idx][buy_flag][cap] = profit

            return dp_arr[idx][buy_flag][cap]
        
        x = rec_trade(0, 1, 2)
        return x
```

### With Dynamic Programing (Tabulation)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(size+1)]

        for idx in range(size-1, -1, -1):
            for buy_flag in range(2):
                for cap in range(1, 3):

                    if buy_flag:
                        target = max(-prices[idx] + dp_arr[idx+1][0][cap] , dp_arr[idx+1][1][cap])
                    else:
                        target = max(prices[idx] + dp_arr[idx+1][1][cap-1], dp_arr[idx+1][0][cap])

                    dp_arr[idx][buy_flag][cap] = target

        return dp_arr[0][1][2]
```

### With Dynamic Programing (Space Optimized)

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        prev_arr = [[0 for _ in range(3)] for _ in range(2)]

        for idx in range(size-1, -1, -1):
            cur_arr = [[0 for _ in range(3)] for _ in range(2)]

            for buy_flag in range(2):
                for cap in range(1, 3):

                    if buy_flag:
                        target = max(-prices[idx] + prev_arr[0][cap] , prev_arr[1][cap])
                    else:
                        target = max(prices[idx] + prev_arr[1][cap-1], prev_arr[0][cap])

                    cur_arr[buy_flag][cap] = target
            
            prev_arr = cur_arr

        return prev_arr[1][2]
```