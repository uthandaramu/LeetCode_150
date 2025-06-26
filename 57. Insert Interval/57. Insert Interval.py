class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        size = len(intervals)

        out = []
        i = 0

        # Non Overlaping left part
        while i < size and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1

        # Overlaping middle part
        while i < size and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        out.append(newInterval)

        # Non Overlaping left part
        while i < size:
            out.append(intervals[i])
            i += 1

        return out