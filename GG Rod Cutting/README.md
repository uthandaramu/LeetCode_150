### Rod Cutting

Given a rod of length n inches and an array price[], where price[i] denotes the value of a piece of length i. Your task is to determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: n = size of price, and price[] is 1-indexed array.

**Example:**

Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]  
Output: 22  
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5 + 17 = 22.

Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]  
Output: 24  
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1] = 8*3 = 24.

Input: price[] = [3]  
Output: 3  
Explanation: There is only 1 way to pick a piece of length 1.

**Constraints:**

1 ≤ price.size() ≤ 103  
1 ≤ price[i] ≤ 106  

**Expected Complexities** 

Time Complexity: O(n^2)  
Auxiliary Space: O(n)  

### WIth Recursion

```python
#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        
        size = len(price)
        
        def rec_cut(idx, capacity):
            if idx == 0:
                if capacity >= 1:
                    return capacity * price[idx]
                else:
                    return 0
            not_pick = rec_cut(idx-1, capacity)
            pick = 0
            if capacity >= idx+1:
                pick = price[idx] + rec_cut(idx, (capacity-(idx+1)))
        
            return max(pick, not_pick)
    
        x = rec_cut(size-1, size)
        return x
```


### With Dynamic Programing

```python
#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        
        size = len(price)
        
        dp_arr = [[-1 for _ in range(size+1)] for _ in range(size)]
        
        def rec_cut(idx, capacity):
            if idx == 0:
                if capacity >= 1:
                    return capacity * price[idx]
                else:
                    return 0
            if dp_arr[idx][capacity] == -1:
                not_pick = rec_cut(idx-1, capacity)
                pick = 0
                if capacity >= idx+1:
                    pick = price[idx] + rec_cut(idx, (capacity-(idx+1)))
                dp_arr[idx][capacity] = max(pick, not_pick)
            return dp_arr[idx][capacity]
    
        x = rec_cut(size-1, size)
        return x
```

### With Dynamic Programing(Tabulation)

```python
# User function Template for python3

class Solution:
    def cutRod(self, price):
        # code here

        size = len(price)

        dp_arr = [[0 for _ in range(size + 1)] for _ in range(size)]

        for cap in range(size + 1):
            dp_arr[0][cap] = (cap) * price[0]

        for idx in range(1, size):
            for capacity in range(size + 1):
                not_pick = dp_arr[idx - 1][capacity]
                pick = 0
                if capacity >= idx + 1:
                    pick = price[idx] + dp_arr[idx][capacity - (idx + 1)]
                dp_arr[idx][capacity] = max(pick, not_pick)

        return dp_arr[size - 1][size]
```

### Dynamic Programing (Space Optimized)

```python
#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        
        size = len(price)
        
        prev_arr = [0 for _ in range(size+1)]
        
        for cap in range(size+1):
            prev_arr[cap] = (cap) * price[0]
        
        for idx in range(1, size):
            cur_arr = [0 for _ in range(size+1)]
            for capacity in range(size+1):
                not_pick = prev_arr[capacity]
                pick = 0
                if capacity >= idx+1:
                    pick = price[idx] + cur_arr[capacity - (idx+1)]
                cur_arr[capacity] = max(pick, not_pick)
            prev_arr = cur_arr
                
        return prev_arr[size]
```