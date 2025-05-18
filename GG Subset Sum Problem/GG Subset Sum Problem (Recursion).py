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