### Subset Sum Problem

Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum. 

**Examples:**  

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9  
Output: true   
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.  

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30  
Output: false  
Explanation: There is no subset with target sum 30.  

Input: arr[] = [1, 2, 3], sum = 6  
Output: true  
Explanation: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.  

**Constraints:**  
1 <= arr.size() <= 200  
1<= arr[i] <= 200  
1<= sum <= 104  

### With Recursion

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        # code here

        size = len(arr)

        def rec_subset(idx, target):
            if target == 0:
                return True
            if idx == 0:
                return arr[idx] == target

            not_take = rec_subset(idx - 1, target)
            take = False
            if target >= arr[idx]:
                take = rec_subset(idx - 1, target - arr[idx])

            return take or not_take

        return (rec_subset(size - 1, sum))
```

### With Dynamic Programing

```python
class Solution:
    def isSubsetSum(self, arr, sum):
        # code here 

        size = len(arr)

        dp_arr = [[-1 for _ in range(sum + 1)] for _ in range(len(arr))]

        def rec_subset(idx, target):
            if target == 0:
                return True
            if idx == 0:
                return arr[idx] == target
            if dp_arr[idx][target] == -1:
                not_take = rec_subset(idx - 1, target)
                take = False
                if target >= arr[idx]:
                    take = rec_subset(idx - 1, target - arr[idx])
                dp_arr[idx][target] = take or not_take
            return dp_arr[idx][target]

        return (rec_subset(size - 1, sum))
```

### With Tabulation

```python
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        
        size = len(arr)
        
        dp_arr = [[False for _ in range(sum+1)] for _ in range(len(arr))]        
        
        for i in range (len(arr)):
            dp_arr[i][0] = True
        if arr[0] <= sum:    
            dp_arr[0][arr[0]] = True
        
        for idx in range(1, size):
            for target in range(1, sum+1):
                not_take = dp_arr[idx-1][target]
                take  = False
                if target >= arr[idx]:
                    take = dp_arr[idx-1][target - arr[idx]]
                dp_arr[idx][target] = take or not_take
        return dp_arr[size-1][sum]
```

### Dynamic Programming (Space optimized)

```python
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        
        size = len(arr)
        
        prev_arr = [False for _ in range(sum+1)]    
        
        prev_arr[0] = True
        
        if arr[0] <= sum:    
            prev_arr[arr[0]] = True
        
        for idx in range(1, size):
            cur_arr = [False for _ in range(sum+1)] 
            cur_arr[0] = True
            for target in range(1, sum+1):
                not_take = prev_arr[target]
                take  = False
                if target >= arr[idx]:
                    take = prev_arr[target - arr[idx]]
                cur_arr[target] = take or not_take
            
            prev_arr = cur_arr
        return prev_arr[sum]
```
