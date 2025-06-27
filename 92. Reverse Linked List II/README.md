### 92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" width="300">

Input: head = [1,2,3,4,5], left = 2, right = 4  
Output: [1,4,3,2,5]

**Example 2:**

Input: head = [5], left = 1, right = 1  
Output: [5]

**Constraints:**

* The number of nodes in the list is n.
* 1 <= n <= 500
* -500 <= Node.val <= 500
* 1 <= left <= right <= n
 

Follow up: Could you do it in one pass?

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        count = 1
        dummy_node = ListNode(0, head)
        leftPrev = dummy_node
        cur_node = head

        #Placing my left pointer in left index and prevLeft in previous to left
        for _ in range(left-1):
            leftPrev, cur_node = cur_node, cur_node.next
        
        #breaking the next pointer and reversing the focus nodes
        prev = None
        for _ in range(right - left + 1):
            tempNext = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = tempNext
        
        #rejoining the reversed node with unaltered node
        leftPrev.next.next = cur_node
        leftPrev.next = prev

        return dummy_node.next
```