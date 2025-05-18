class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)

        dp_arr = [[0 for _ in range(W + 1)] for _ in range(size)]

        for i in range(wt[0], W + 1):
            dp_arr[0][i] = val[0]

        for idx in range(1, size):
            for weight in range(W + 1):
                not_pick = 0 + dp_arr[idx - 1][weight]
                pick = 0
                if wt[idx] <= weight:
                    pick = val[idx] + dp_arr[idx - 1][weight - wt[idx]]
                dp_arr[idx][weight] = max(pick, not_pick)

        return dp_arr[size - 1][W]


# {
# Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends