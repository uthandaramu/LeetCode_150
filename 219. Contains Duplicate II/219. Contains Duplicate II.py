class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size = len(nums)
        i = prev = 0
        visited = set()

        for i in range(size):

            if nums[i] in visited:
                return True

            visited.add(nums[i])

            if i - prev >= k:
                visited.remove(nums[prev])
                prev += 1

        return False