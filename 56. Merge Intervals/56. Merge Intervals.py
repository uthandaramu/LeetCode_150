class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        size = len(intervals)
        result = [intervals[0]]
        i = 1

        while i < size:

            if result[-1][1] >= intervals[i][0]:
                minInterval = min(result[-1][0], intervals[i][0])
                maxInterval = max(result[-1][1], intervals[i][1])
                result[-1] = [minInterval, maxInterval]

            else:
                result.append(intervals[i])
            i += 1

        return (result)