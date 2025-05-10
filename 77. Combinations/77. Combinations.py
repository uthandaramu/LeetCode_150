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
