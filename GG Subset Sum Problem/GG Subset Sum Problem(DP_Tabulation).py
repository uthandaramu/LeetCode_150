class Solution:
    def isSubsetSum(self, arr, sum):
        # code here

        size = len(arr)

        dp_arr = [[False for _ in range(sum + 1)] for _ in range(len(arr))]

        for i in range(len(arr)):
            dp_arr[i][0] = True
        if arr[0] <= sum:
            dp_arr[0][arr[0]] = True

        for idx in range(1, size):
            for target in range(1, sum + 1):
                not_take = dp_arr[idx - 1][target]
                take = False
                if target >= arr[idx]:
                    take = dp_arr[idx - 1][target - arr[idx]]
                dp_arr[idx][target] = take or not_take
        return dp_arr[size - 1][sum]