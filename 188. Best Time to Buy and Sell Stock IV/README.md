### 188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**  

Input: k = 2, prices = [2,4,1]  
Output: 2  
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

**Example 2:**

Input: k = 2, prices = [3,2,6,5,0,3]  
Output: 7  
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

**Constraints:**

1 <= k <= 100  
1 <= prices.length <= 1000  
0 <= prices[i] <= 1000  

### With Recursion

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        def rec_trade(idx, buy_flag, cap):

            if cap == 0 or idx == size:
                return 0

            if buy_flag:
                profit = max(-prices[idx] + rec_trade(idx+1, 0, cap), rec_trade(idx+1, 1, cap))

            else:
                profit = max(prices[idx] + rec_trade(idx+1, 1, cap-1), rec_trade(idx+1, 0, cap))
            
            return profit
        
        x = rec_trade(0, 1, k)
        return x
```

### With Dynamic Programing

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(size)]

        def rec_trade(idx, buy_flag, cap):

            if cap == 0 or idx == size:
                return 0

            if dp_arr[idx][buy_flag][cap] == -1:
                if buy_flag:
                    profit = max(-prices[idx] + rec_trade(idx+1, 0, cap), rec_trade(idx+1, 1, cap))

                else:
                    profit = max(prices[idx] + rec_trade(idx+1, 1, cap-1), rec_trade(idx+1, 0, cap))

                dp_arr[idx][buy_flag][cap] = profit

            return dp_arr[idx][buy_flag][cap]
        
        x = rec_trade(0, 1, k)
        return x
```

### With Dynamic Programing (Tabulation)

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        dp_arr = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(size+1)]

        for idx in range(size-1, -1, -1):
            for buy_flag in range(2):
                for cap in range(1, k+1):
                    if buy_flag:
                        profit = max(-prices[idx] + dp_arr[idx+1][0][cap] , dp_arr[idx+1][1][cap])
                    else:
                        profit = max(prices[idx] + dp_arr[idx+1][1][cap-1] , dp_arr[idx+1][0][cap])

                    dp_arr[idx][buy_flag][cap] = profit
        
        return dp_arr[0][1][k]
```

### With Dynamic Programing (Space Optimized)

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)

        prev_arr = [[0 for _ in range(k+1)] for _ in range(2)]

        for idx in range(size-1, -1, -1):
            cur_arr = [[0 for _ in range(k+1)] for _ in range(2)]
            for buy_flag in range(2):
                for cap in range(1, k+1):
                    if buy_flag:
                        profit = max(-prices[idx] + prev_arr[0][cap] , prev_arr[1][cap])
                    else:
                        profit = max(prices[idx] + prev_arr[1][cap-1] , prev_arr[0][cap])

                    cur_arr[buy_flag][cap] = profit
            
            prev_arr = cur_arr
        
        return prev_arr[1][k]
```