### 77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

**Example 1:**

Input: n = 4, k = 2  
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]  
Explanation: There are 4 choose 2 = 6 total combinations.  
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.  

**Example 2:**

Input: n = 1, k = 1  
Output: [[1]]  
Explanation: There is 1 choose 1 = 1 total combination.
 

**Constraints:**

1 <= n <= 20  
1 <= k <= n  

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        out_arr = []
        storage_arr = []
        def helpCombine(start, storage_arr):
            if len(storage_arr) == k:
                out_arr.append(storage_arr[:])
                return
            for i in range (start, n+1):
                storage_arr.append(i)
                helpCombine(i+1, storage_arr)
                storage_arr.pop()

        helpCombine(1, storage_arr)
        return out_arr

```