### 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]  
**Output:** [1,1,2,3,4,4,5,6]  
**Explanation:** The linked-lists are:  
[  
  1->4->5,  
  1->3->4,  
  2->6  
]  
merging them into one sorted list:  
1->1->2->3->4->4->5->6

**Example 2:**

**Input:** lists = []  
**Output:** []

**Example 3:**

**Input:** lists = [[]]  
**Output:** []

**Constraints:**

* k == lists.length
* 0 <= k <= 104
* 0 <= lists[i].length <= 500
* -104 <= lists[i][j] <= 104
* lists[i] is sorted in ascending order.
* The sum of lists[i].length will not exceed 104.

#### Note : The same problem can be solved with merge two sorted list approach where output of merged one needs to be merged with next one.

#### But below one is most optimized one with priority queue

```python
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        size = len(lists)

        minHeap = []

        for i in range(size):
            if lists[i]:
                val = lists[i].val
                heapq.heappush(minHeap, (val, lists[i]))

        dummy_node = out_ptr = ListNode(-1)

        while minHeap:

            _, top_node = heapq.heappop(minHeap)
            out_ptr.next = top_node
            if top_node.next:
                val = top_node.next.val
                heapq.heappush(minHeap, (val, top_node.next))

            out_ptr = out_ptr.next

        return dummy_node.next
```