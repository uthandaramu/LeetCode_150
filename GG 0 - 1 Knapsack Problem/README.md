### 0 - 1 Knapsack Problem

Given n items, each with a specific weight and value, and a knapsack with a capacity of W, the task is to put the items in the knapsack such that the sum of weights of the items <= W and the sum of values associated with them is maximized. 

Note: You can either place an item entirely in the bag or leave it out entirely. Also, each item is available in single quantity.

**Examples :**

Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]   
Output: 3  
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.  

Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]   
Output: 0  
Explanation: Every item has a weight exceeding the knapsack's capacity (3).  

Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3]   
Output: 80  
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.  

**Constraints:**  

2 ≤ val.size() = wt.size() ≤ 103  
1 ≤ W ≤ 103  
1 ≤ val[i] ≤ 103  
1 ≤ wt[i] ≤ 103

### With Recursion

```python
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)
        
        def rec_steal(idx, weight):
            if idx == 0:
                if weight >= wt[idx]:
                    return val[idx]
                else:
                    return 0
            
            not_pick = 0 + rec_steal(idx-1, weight)
            pick = 0
            if weight >= wt[idx]:
                pick = val[idx] + rec_steal(idx-1, weight-wt[idx])
            
            return max(not_pick, pick)
        
        x = rec_steal(size-1, W)
        return x

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
```

### With Dynamic Programing

```python
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)
        
        dp_arr = [[-1 for _ in range(W+1)] for _ in range(size)]
        
        def rec_steal(idx, weight):
            if idx == 0:
                if weight >= wt[idx]:
                    return val[idx]
                else:
                    return 0
            if dp_arr[idx][weight] == -1:
                not_pick = 0 + rec_steal(idx-1, weight)
                pick = 0
                if weight >= wt[idx]:
                    pick = val[idx] + rec_steal(idx-1, weight-wt[idx])
                dp_arr[idx][weight] = max(not_pick, pick)
            return dp_arr[idx][weight]
        
        x = rec_steal(size-1, W)
        return x

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
```

### With Dynamic Programing(Tabulation)

```python
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)

        dp_arr = [[0 for _ in range(W + 1)] for _ in range(size)]

        for i in range(wt[0], W + 1):
            dp_arr[0][i] = val[0]

        for idx in range(1, size):
            for weight in range(W + 1):
                not_pick = 0 + dp_arr[idx - 1][weight]
                pick = 0
                if wt[idx] <= weight:
                    pick = val[idx] + dp_arr[idx - 1][weight - wt[idx]]
                dp_arr[idx][weight] = max(pick, not_pick)

        return dp_arr[size - 1][W]


# { 
# Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
```

### With Dynamic Programing (Space Optimized)

```python
class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)
        
        prev_arr = [0 for _ in range(W+1)]
        
        for i in range(wt[0], W+1):
            prev_arr[i] = val[0]
            
        for idx in range(1, size):
            cur_arr = [0 for _ in range(W+1)]
            for weight in range(W+1):
                not_pick = 0 + prev_arr[weight]
                pick = 0
                if wt[idx] <= weight:
                    pick = val[idx] + prev_arr[weight-wt[idx]]
                cur_arr[weight] = max(pick, not_pick)
            prev_arr = cur_arr
        
        return prev_arr[W]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
```