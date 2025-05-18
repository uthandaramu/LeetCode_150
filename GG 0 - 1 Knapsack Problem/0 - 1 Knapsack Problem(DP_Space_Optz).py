class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)

        prev_arr = [0 for _ in range(W + 1)]

        for i in range(wt[0], W + 1):
            prev_arr[i] = val[0]

        for idx in range(1, size):
            cur_arr = [0 for _ in range(W + 1)]
            for weight in range(W + 1):
                not_pick = 0 + prev_arr[weight]
                pick = 0
                if wt[idx] <= weight:
                    pick = val[idx] + prev_arr[weight - wt[idx]]
                cur_arr[weight] = max(pick, not_pick)
            prev_arr = cur_arr

        return prev_arr[W]


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