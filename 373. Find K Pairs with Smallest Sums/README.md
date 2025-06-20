### 373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

**Example 1:**

**Input:** nums1 = [1,7,11], nums2 = [2,4,6], k = 3  
**Output:** [[1,2],[1,4],[1,6]]  
**Explanation:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

**Example 2:**

**Input:** nums1 = [1,1,2], nums2 = [1,2,3], k = 2  
**Output:** [[1,1],[1,1]]  
**Explanation:** The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

**Constraints:**

* 1 <= nums1.length, nums2.length <= 105
* -109 <= nums1[i], nums2[i] <= 109
* nums1 and nums2 both are sorted in non-decreasing order.
* 1 <= k <= 104
* k <= nums1.length * nums2.length

### With Extra Visited space

```python
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        out = []
        size1 = len(nums1)
        size2 = len(nums2)

        # To avoid repeatative combinations
        visited = set()

        i = j = 0
        minHeap = []

        #To keep a track of minimum sum combinations
        heapq.heappush(minHeap, (nums1[0]+nums2[0], 0, 0))

        out = []

        count = 0
        
        while minHeap and (i < size1 or j < size2) and count < k:

            total, first, second = heapq.heappop(minHeap)
            out.append([nums1[first], nums2[second]])

            #(i+1, j) combination
            if (first+1, second) not in visited and first+1 < size1:
                total = nums1[first+1] + nums2[second]
                heapq.heappush(minHeap, (total, first+1, second))
                visited.add((first+1, second))

            #(i, j+1) combination
            if (first, second+1) not in visited and second+1 < size2:
                total = nums1[first] + nums2[second+1]
                heapq.heappush(minHeap, (total, first, second+1))
                visited.add((first, second+1))

            #Tracking K values    
            count += 1

        return (out)
```

### Without extra visited space (Space Optimized)

```python
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        size1 = len(nums1)
        size2 = len(nums2)

        minHeap = []
        
        #Add all elements in first array paring with oth index element in second array
        i = 0
        while i < size1 and i < k:
            total = nums1[i] + nums2[0]
            heapq.heappush(minHeap, (total, i, 0))
            i += 1

        count = 0
        out = []
        while heapq and count < k:

            total, i, j = heapq.heappop(minHeap)
            out.append([nums1[i], nums2[j]])
            
            #Since we have all first array elements in pair, it is required to iterate elements in second array which can avoid duplicate paring
            if j + 1 < size2:
                total = nums1[i] + nums2[j + 1]
                heapq.heappush(minHeap, (total, i, j + 1))

            count += 1

        return (out)
```