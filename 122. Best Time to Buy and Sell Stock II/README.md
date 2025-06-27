### 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

**Example 1:**

Input: prices = [7,1,5,3,6,4]  
Output: 7  
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.  
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.  
Total profit is 4 + 3 = 7.  

**Example 2:**

Input: prices = [1,2,3,4,5]  
Output: 4  
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.  
Total profit is 4.  

**Example 3:**

Input: prices = [7,6,4,3,1]  
Output: 0  
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

**Constraints:**

1 <= prices.length <= 3 * 104  
0 <= prices[i] <= 104

### with Recursion

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        def rec_trade(idx, buy_flag):
            if idx == size:
                return 0
            if buy_flag:
                profit = max((-prices[idx] + rec_trade(idx+1, 0)), (rec_trade(idx+1, 1)))
            else:
                profit = max((prices[idx] + rec_trade(idx+1, 1)),(rec_trade(idx+1, 0)))

            return profit
        
        x = rec_trade(0, 1)
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

        dp_arr = [[-1 for _ in range(2)] for _ in range(size)]

        def rec_trade(idx, buy_flag):
            if idx == size:
                return 0
            if dp_arr[idx][buy_flag] == -1:
                if buy_flag:
                    profit = max((-prices[idx] + rec_trade(idx+1, 0)), (rec_trade(idx+1, 1)))
                else:
                    profit = max((prices[idx] + rec_trade(idx+1, 1)),(rec_trade(idx+1, 0)))
                
                dp_arr[idx][buy_flag] = profit

            return dp_arr[idx][buy_flag]
        
        x = rec_trade(0, 1)
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

        dp_arr = [[0 for _ in range(2)] for _ in range(size+1)]

        dp_arr[size][0] = dp_arr[size][1] = 0

        for idx in range(size-1, -1, -1):
            for buy_flag in range(0, 2):

                if buy_flag:
                    profit = max((-prices[idx] + dp_arr[idx+1][0]), (dp_arr[idx+1][1]))
                else:
                    profit = max((prices[idx] + dp_arr[idx+1][1]),(dp_arr[idx+1][0]))
                
                dp_arr[idx][buy_flag] = profit

        return dp_arr[0][1]
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

        prev_arr = [0 for _ in range(2)]

        for idx in range(size-1, -1, -1):
            cur_arr = [0 for _ in range(2)]
            for buy_flag in range(0, 2):
                if buy_flag:
                    profit = max((-prices[idx] + prev_arr[0]), (prev_arr[1]))
                else:
                    profit = max((prices[idx] + prev_arr[1]),(prev_arr[0]))

                cur_arr[buy_flag] = profit
            prev_arr = cur_arr

        return prev_arr[1]
```

### Most Optimal

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += prices[i] - buy
            buy = prices[i]
        return profit
```