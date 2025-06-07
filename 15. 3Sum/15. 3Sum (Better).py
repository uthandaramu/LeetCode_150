class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        out_set = set()
        for i in range(size):
            temp_dict = {}
            for j in range(i + 1, size):
                target = - (nums[i] + nums[j])
                if target in temp_dict:
                    out_set.add(tuple(sorted((nums[i], nums[j], target))))
                else:
                    temp_dict[nums[j]] = 1

        return list(out_set)