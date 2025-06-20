class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)

        out = [1 for _ in range(size)]

        # Prefix operation
        pre = 1
        out[0] = pre
        for i in range(1, size):
            out[i] = pre * nums[i - 1]
            pre = out[i]

        # Postfix operation
        post = 1
        for i in range(size - 1, -1, -1):
            out[i] = post * out[i]
            post = post * nums[i]

        return (out)