class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        target_index = size - k

        # Quick Select Approach (using array partioning)
        def rec_k(start, end):
            pivot = end
            pointer = start

            for idx in range(start, end):
                if nums[idx] <= nums[pivot]:
                    nums[idx], nums[pointer] = nums[pointer], nums[idx]
                    pointer += 1

            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]

            if pointer == (size - k):
                return nums[pointer]
            elif pointer > (size - k):
                return rec_k(start, pointer - 1)
            else:
                return rec_k(pointer + 1, end)

        return (rec_k(0, size - 1))