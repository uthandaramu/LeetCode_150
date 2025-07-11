### 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

**Example 1:**

**Input:** nums1 = [1,3], nums2 = [2]  
**Output:** 2.00000  
**Explanation:** merged array = [1,2,3] and median is 2.

**Example 2:**

**Input:** nums1 = [1,2], nums2 = [3,4]  
**Output:** 2.50000  
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

**Constraints:**

* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* -106 <= nums1[i], nums2[i] <= 106

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #Intiuation: Binary search

        #Having smaller array as first for small optimal searching 
        a = nums1
        b = nums2
        if len(nums2) < len(nums1):
            a = nums2
            b = nums1

        size1 = len(a)
        size2 = len(b)
        totalSize = size1 + size2

        #Symmetrical size same formula for both odd and even length
        partLength = (totalSize + 1) // 2

        #Focus primarily on idex to split in first array, rest can be computed along with
        left, right = 0, len(a)
        
        while left <= right:

            mid1 = (left + right) // 2
            mid2 = partLength -  mid1

            #Seperating the array into left and right half (l1 and r1, l2 and r2)
            #Edge cases if can't split to make the symmetrical end array
            r1 = r2 = 10 ** 6
            l1 = l2 = -r1

            #Assigning l1 and r1 if valid
            if (mid1 < size1): r1 = a[mid1]
            if ((mid1 - 1) > -1): l1 = a[mid1-1]

            #Assigning l2 and r2 if valid
            if (mid2 < size2): r2 = b[mid2]
            if ((mid2-1) > -1): l2 = b[mid2-1]

            #cheking cross values if left side has smaller values than left values
            if l1 <= r2 and l2 <= r1:
                #proper symmetry
                #differentiate between odd and even total Length arr
                #even case
                if not totalSize % 2:
                    #Avg(max of left side and min of right side)
                    result = (max(l1, l2) + min(r1, r2)) / 2.0
                
                #odd case
                else:
                    result = max(l1, l2)
                
                return result

            elif l1 > r2:
                #my mid in first arr is in left side
                right = mid1 - 1
            
            else:
                #my mid in first arr is in right side
                left = mid1 + 1
```