class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        k = 1
        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])