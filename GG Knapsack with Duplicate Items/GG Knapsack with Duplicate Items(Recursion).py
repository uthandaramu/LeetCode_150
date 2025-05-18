# User function Template for python3

class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        size = len(val)

        def max_knapsack(idx, capacity):
            if idx == 0:
                if capacity >= wt[idx]:
                    return val[idx] * (capacity // wt[idx])
                else:
                    return 0
            not_pick = max_knapsack(idx - 1, capacity)
            pick = 0
            if wt[idx] <= capacity:
                pick = val[idx] + max_knapsack(idx, capacity - wt[idx])

            return max(pick, not_pick)

        x = max_knapsack(size - 1, capacity)

        return x


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        W = int(input())
        val = list(map(int, input().split()))
        wt = list(map(int, input().split()))

        ob = Solution()
        print(ob.knapSack(val, wt, W))
        print("~")

# } Driver Code Ends