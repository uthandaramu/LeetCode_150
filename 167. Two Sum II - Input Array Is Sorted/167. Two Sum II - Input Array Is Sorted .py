class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Using Hashing

        size = len(numbers)
        hash_dict = {}
        out_arr = []

        for idx, element in enumerate(numbers):
            hash_dict[element] = idx

        for i in range(size):
            if target-numbers[i] in hash_dict:
                out_arr.append(hash_dict[target-numbers[i]]+1)
                out_arr.append(i+1)
                return sorted(out_arr)
