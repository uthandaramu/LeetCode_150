### Perfect Sum Problem

Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

**Examples:**

Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10  
Output: 3  
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.  

Input: arr[] = [2, 5, 1, 4, 3], target = 10  
Output: 3  
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.  

Input: arr[] = [5, 7, 8], target = 3  
Output: 0  
Explanation: There are no subsets of the array that sum up to the target 3.  

Input: arr[] = [35, 2, 8, 22], target = 0  
Output: 1  
Explanation: The empty subset is the only subset with a sum of 0.  

**Constraints:**

1 ≤ arr.size() ≤ 103  
0 ≤ arr[i] ≤ 103  
0 ≤ target ≤ 103   

### With Dynamic Programming

```python
# User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        nums = arr
        size = len(nums)

        dp_arr = [[-1 for _ in range(target + 1)] for _ in range(size)]

        def rec_count(idx, target):
            if idx == 0:
                if target == 0 and nums[0] == 0:
                    return 2
                if target == 0 or nums[0] == target:
                    return 1
                return 0
            if dp_arr[idx][target] == -1:
                not_take = rec_count(idx - 1, target)
                take = 0
                if nums[idx] <= target:
                    take = rec_count(idx - 1, target - nums[idx])
                dp_arr[idx][target] = (take + not_take)
            return dp_arr[idx][target]

        return (rec_count(size - 1, target))


# {
# Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends
```