class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        prev_arr = triangle[-1]
        for i in range(row-2, -1, -1):
            cur_arr=[0 for _ in range(i+1)]
            for j in range(i, -1, -1):
                up = triangle[i][j] + prev_arr[j]
                diagnol = triangle[i][j] + prev_arr[j+1]
                cur_arr[j] = min(up, diagnol)
            prev_arr = cur_arr
        return (prev_arr[0])