class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort()
        size = result = len(points)
        prev = points[0]

        for i in range(1, size):
            curr = points[i]
            if prev[1] >= curr[0]:
                result -= 1
                prev = [max(prev[0], curr[0]), min(prev[1], curr[1])]
            else:
                prev = curr

        return (result)