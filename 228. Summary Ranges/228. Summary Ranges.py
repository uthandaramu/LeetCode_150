from collections import deque
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        size = len(nums)
        if size == 0:
            return nums
        stack = deque()
        i = 0
        out_arr = []
        while i < size:
            if stack and nums[i] != stack[-1]+1:
                if len(stack) == 1:
                    out_arr.append(str(stack.pop()))
                else:
                    out_arr.append(str(stack[0]) + "->" + str(stack[-1]))
                stack.clear()
            stack.append(nums[i])
            i += 1
        if len(stack) == 1:
            out_arr.append(str(stack.pop()))
        else:
            out_arr.append(str(stack[0]) + "->" + str(stack[-1]))
        return out_arr