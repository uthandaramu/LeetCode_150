# User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        nums = arr
        size = len(nums)

        dp_arr = [[-1 for _ in range(target + 1)] for _ in range(size)]

        def rec_count(idx, target):
            if idx == 0:
                if target == 0 and nums[0] == 0:
                    return 2
                if target == 0 or nums[0] == target:
                    return 1
                return 0
            if dp_arr[idx][target] == -1:
                not_take = rec_count(idx - 1, target)
                take = 0
                if nums[idx] <= target:
                    take = rec_count(idx - 1, target - nums[idx])
                dp_arr[idx][target] = (take + not_take)
            return dp_arr[idx][target]

        return (rec_count(size - 1, target))


# {
# Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends