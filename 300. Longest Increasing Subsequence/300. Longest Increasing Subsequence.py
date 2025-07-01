class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subArr = [nums[0]]
        size = len(nums)

        for i in range(1, size):
            
            #Place nums in incremental order
            if nums[i] > subArr[-1]:
                subArr.append(nums[i])

            else:
                #If not find the place to replace the element i.e., find the lower bound position
                start = 0
                end = len(subArr)

                while start <= end:
                    mid = (start + end) // 2
                    if nums[i] <= subArr[mid]:
                        end = mid - 1
                        idx = mid
                    else:
                        start = mid + 1

                subArr[idx] = nums[i]
            
        return len(subArr)