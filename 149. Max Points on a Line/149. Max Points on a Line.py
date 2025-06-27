from fractions import Fraction
from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        size = len(points)

        max_points = 1

        for i in range(size):
            hash_slope = defaultdict(int)
            point1 = points[i]

            for j in range(i + 1, size):
                point2 = points[j]

                if point1[0] == point2[0]:
                    slope = "inf"
                else:
                    slope = Fraction((point2[1] - point1[1]), (point2[0] - point1[0]))

                hash_slope[slope] += 1

                max_points = max(max_points, hash_slope[slope] + 1)

        return max_points