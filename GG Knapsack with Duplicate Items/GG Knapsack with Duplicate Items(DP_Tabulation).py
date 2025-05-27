# User function Template for python3

class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        size = len(val)

        dp_arr = [[0 for _ in range(capacity + 1)] for _ in range(size)]

        for cap in range(capacity + 1):
            if cap >= wt[0]:
                dp_arr[0][cap] = (cap // wt[0]) * val[0]

        for idx in range(1, size):
            for cap in range(capacity + 1):
                not_pick = dp_arr[idx - 1][cap]
                pick = 0
                if wt[idx] <= cap:
                    pick = val[idx] + dp_arr[idx][cap - wt[idx]]

                dp_arr[idx][cap] = max(pick, not_pick)

        return dp_arr[size - 1][capacity]


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