class Solution(object):
    def find_combinations(self, input_arr, idx, target, out_arr, storage_arr):
        if idx == len(input_arr):
            if target == 0:
                out_arr.append(storage_arr[:])
            return
        if input_arr[idx] <= target:
            storage_arr.append(input_arr[idx])
            self.find_combinations(input_arr, idx, target - input_arr[idx], out_arr, storage_arr)
            storage_arr.pop()
        self.find_combinations(input_arr, idx + 1, target, out_arr, storage_arr)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out_arr = []
        storage_arr = []
        self.find_combinations(candidates, 0, target, out_arr, storage_arr)
        return out_arr
