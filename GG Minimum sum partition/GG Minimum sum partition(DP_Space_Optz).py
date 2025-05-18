# User function Template for python3
class Solution:
    def minDifference(self, arr):
        # code here
        total_sum = sum(arr)
        size = len(arr)
        prev_arr = [False for _ in range(total_sum + 1)]
        prev_arr[0] = True

        if arr[0] <= total_sum:
            prev_arr[arr[0]] = True

        for idx in range(1, size):
            cur_arr = [False for _ in range(total_sum + 1)]
            cur_arr[0] = True
            for target in range(total_sum + 1):
                not_take = prev_arr[target]
                take = False
                if arr[idx] <= target:
                    take = prev_arr[target - arr[idx]]
                cur_arr[target] = take or not_take

            prev_arr = cur_arr

        mini = 1e8

        for idx, value in enumerate(prev_arr):
            if value:
                s1 = idx
                s2 = total_sum - idx
                diff = abs(s1 - s2)
                mini = min(mini, diff)

        return mini


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minDifference(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends