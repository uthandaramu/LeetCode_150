### Knapsack with Duplicate Items

Given a set of items, each with a weight and a value, represented by the array wt and val respectively. Also, a knapsack with a weight limit capacity.  
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.  
Note: Each item can be taken any number of times.  

**Examples:**

Input: val = [1, 1], wt = [2, 1], capacity = 3  
Output: 3  
Explanation: The optimal choice is to pick the 2nd element 3 times.  

Input: val[] = [6, 1, 7, 7], wt[] = [1, 3, 4, 5], capacity = 8  
Output: 48  
Explanation: The optimal choice is to pick the 1st element 8 times.  

Input: val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1  
Output: 0  
Explanation: We can't pick any element .hence, total profit is 0.

**Constraints:**

1 <= val.size() = wt.size() <= 1000  
1 <= capacity <= 1000  
1 <= val[i], wt[i] <= 100  

### With Recursion

```python
#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        size = len(val)
        
        def max_knapsack(idx, capacity):
            if idx == 0:
                if capacity >= wt[idx]:
                    return val[idx] * (capacity//wt[idx])
                else:
                    return 0
            not_pick = max_knapsack(idx-1, capacity)
            pick = 0
            if wt[idx] <= capacity:
                pick = val[idx] + max_knapsack(idx, capacity - wt[idx])
            
            return max(pick, not_pick)
        
        x = max_knapsack(size-1, capacity)
        
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
```

### With Dynamic Programing

```python
#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        size = len(val)
        
        dp_arr = [[-1 for _ in range(capacity+1)] for _ in range(size)]
        
        def max_knapsack(idx, capacity):
            if idx == 0:
                if capacity >= wt[idx]:
                    return val[idx] * (capacity//wt[idx])
                else:
                    return 0
            if dp_arr[idx][capacity] == -1:
                not_pick = max_knapsack(idx-1, capacity)
                pick = 0
                if wt[idx] <= capacity:
                    pick = val[idx] + max_knapsack(idx, capacity - wt[idx])
                dp_arr[idx][capacity] = max(pick, not_pick)
                
            return dp_arr[idx][capacity]
        
        x = max_knapsack(size-1, capacity)
        
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
```

### With Dynamic Programing (Tabulation)

```python
#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        size = len(val)
        
        dp_arr = [[0 for _ in range(capacity+1)] for _ in range(size)]
        
        for cap in range(capacity+1):
            if cap >= wt[0]:
                dp_arr[0][cap] = (cap // wt[0]) * val[0]

        
        for idx in range(1, size):
            for cap in range(capacity+1):
                not_pick = dp_arr[idx-1][cap]
                pick = 0
                if wt[idx] <= cap:
                    pick = val[idx] + dp_arr[idx][cap - wt[idx]]
                
                dp_arr[idx][cap] = max(pick, not_pick)
            
        return dp_arr[size-1][capacity]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
```

### With Dynamic Programing(Space Optimized)

```python
#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        size = len(val)
        
        prev_arr = [0 for _ in range(capacity+1)] 
        
        for cap in range(capacity+1):
            if cap >= wt[0]:
                prev_arr[cap] = (cap // wt[0]) * val[0]

        
        for idx in range(1, size):
            cur_arr = [0 for _ in range(capacity+1)]
            for cap in range(capacity+1):
                not_pick = prev_arr[cap]
                pick = 0
                if wt[idx] <= cap:
                    pick = val[idx] + cur_arr[cap - wt[idx]]
                
                cur_arr[cap] = max(pick, not_pick)
            prev_arr = cur_arr
            
        return prev_arr[capacity]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends
```