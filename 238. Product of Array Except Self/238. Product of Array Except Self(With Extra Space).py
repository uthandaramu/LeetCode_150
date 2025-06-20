class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        prefix = [1 for _ in range(size)]
        postfix = [1 for _ in range(size)]
        out = [1 for _ in range(size)]

        # prefix operation
        for i in range(size):
            prefix[i] = prefix[i - 1] * nums[i]

        postfix[size - 1] = nums[size - 1]

        for j in range(size - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j]

        for i in range(size):
            if i == 0:
                out[i] = postfix[i + 1]
            elif i == size - 1:
                out[i] = prefix[i - 1]
            else:
                out[i] = prefix[i - 1] * postfix[i + 1]

        return (out)