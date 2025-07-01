class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        prefixMax = [0] * size
        suffixMax = [0] * size

        prefixMax[0] = height[0]
        suffixMax[-1] = height[-1]

        #Identifying prefix max
        for i in range(1, size):
            prefixMax[i] = max(prefixMax[i-1], height[i])
        
        #Identifying suffix max
        for i in range(size-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], height[i])
        
        result = 0
        for i in range(size):
            if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
                result += min(prefixMax[i], suffixMax[i]) - height[i]
        
        return result