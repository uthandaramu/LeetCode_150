class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_arr = [[-1 for _ in range(n)] for _ in range(m)]
        def core_rec(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp_arr[i][j] == -1:
                up = core_rec(i-1, j)
                left = core_rec(i, j-1)
                dp_arr[i][j] = up + left
            return dp_arr[i][j]

        return(core_rec(m-1,n-1))