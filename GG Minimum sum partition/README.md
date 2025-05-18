### Minimum sum partition


Given an array arr[]  containing non-negative integers, the task is to divide it into two sets set1 and set2 such that the absolute difference between their sums is minimum and find the minimum difference.

**Examples:**

**Input:** arr[] = [1, 6, 11, 5]  
**Output:** 1  
**Explanation:**   
Subset1 = {1, 5, 6}, sum of Subset1 = 12   
Subset2 = {11}, sum of Subset2 = 11   
Hence, minimum difference is 1.    

**Input:** arr[] = [1, 4]  
**Output:** 3  
**Explanation:**   
Subset1 = {1}, sum of Subset1 = 1  
Subset2 = {4}, sum of Subset2 = 4  
Hence, minimum difference is 3.

**Input:** arr[] = [1]  
**Output:** 1  
**Explanation:**  
Subset1 = {1}, sum of Subset1 = 1  
Subset2 = {}, sum of Subset2 = 0  
Hence, minimum difference is 1.  

**Constraints:**

1 ≤ arr.size()*|sum of array elements| ≤ 105  
1 <= arr[i] <= 105  

### With Dynamic Programing(Space Optimized)

```python
# User function Template for python3
class Solution:
    def minDifference(self, arr):
        # code here
        total_sum = sum(arr)
        size = len(arr)
        prev_arr = [False for _ in range(total_sum + 1)]
        prev_arr[0] = True

        if arr[0] <= total_sum:
            prev_arr[arr[0]] = True

        for idx in range(1, size):
            cur_arr = [False for _ in range(total_sum + 1)]
            cur_arr[0] = True
            for target in range(total_sum + 1):
                not_take = prev_arr[target]
                take = False
                if arr[idx] <= target:
                    take = prev_arr[target - arr[idx]]
                cur_arr[target] = take or not_take

            prev_arr = cur_arr

        mini = 1e8

        for idx, value in enumerate(prev_arr):
            if value:
                s1 = idx
                s2 = total_sum - idx
                diff = abs(s1 - s2)
                mini = min(mini, diff)

        return mini


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minDifference(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends
```