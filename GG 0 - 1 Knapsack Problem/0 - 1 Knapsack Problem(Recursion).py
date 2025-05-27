class Solution:
    def knapsack(self, W, val, wt):
        # code here
        size = len(val)

        def rec_steal(idx, weight):
            if idx == 0:
                if weight >= wt[idx]:
                    return val[idx]
                else:
                    return 0

            not_pick = 0 + rec_steal(idx - 1, weight)
            pick = 0
            if weight >= wt[idx]:
                pick = val[idx] + rec_steal(idx - 1, weight - wt[idx])

            return max(not_pick, pick)

        x = rec_steal(size - 1, W)
        return x


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