class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev_arr = [0 for _ in range(n)]
        for i in range(m):
            cur_arr = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    cur_arr[j] = 1
                else:
                    cur_arr[j] = prev_arr[j] + cur_arr[j - 1]
            prev_arr = cur_arr

        return (prev_arr[n - 1])