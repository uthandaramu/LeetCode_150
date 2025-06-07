class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            mini = min(height[start], height[end])
            cur_area = mini * (end - start)
            area = max(area, cur_area)
            if height[start] > height[end]:
                end = end - 1
            else:
                start = start + 1

        return area