# User function Template for python3

class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        size = len(val)

        prev_arr = [0 for _ in range(capacity + 1)]

        for cap in range(capacity + 1):
            if cap >= wt[0]:
                prev_arr[cap] = (cap // wt[0]) * val[0]

        for idx in range(1, size):
            cur_arr = [0 for _ in range(capacity + 1)]
            for cap in range(capacity + 1):
                not_pick = prev_arr[cap]
                pick = 0
                if wt[idx] <= cap:
                    pick = val[idx] + cur_arr[cap - wt[idx]]

                cur_arr[cap] = max(pick, not_pick)
            prev_arr = cur_arr

        return prev_arr[capacity]


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