class Solution:
    def isSubsetSum(self, arr, sum):
        # code here

        size = len(arr)

        prev_arr = [False for _ in range(sum + 1)]

        prev_arr[0] = True

        if arr[0] <= sum:
            prev_arr[arr[0]] = True

        for idx in range(1, size):
            cur_arr = [False for _ in range(sum + 1)]
            cur_arr[0] = True
            for target in range(1, sum + 1):
                not_take = prev_arr[target]
                take = False
                if target >= arr[idx]:
                    take = prev_arr[target - arr[idx]]
                cur_arr[target] = take or not_take

            prev_arr = cur_arr
        return prev_arr[sum]