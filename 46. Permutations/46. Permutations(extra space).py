class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        size = len(nums)

        def recPermute(stackSpace, visitedHash):
            if len(stackSpace) == size:
                result.append(list(stackSpace))

            for element in nums:
                if element not in visitedHash:
                    stackSpace.append(element)
                    visitedHash.add(element)
                    recPermute(stackSpace, visitedHash)
                    stackSpace.remove(element)
                    visitedHash.remove(element)

        hashSet = set()
        stack = deque()
        recPermute(stack, hashSet)

        return (result)