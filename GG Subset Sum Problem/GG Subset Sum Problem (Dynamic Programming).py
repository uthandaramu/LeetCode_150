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