### 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" width="300">

Input: head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]

**Example 2:** 

Input: head = [1], n = 1  
Output: []

**Example 3:**

Input: head = [1,2], n = 1  
Output: [1]
 

**Constraints:**

The number of nodes in the list is sz.  
1 <= sz <= 30  
0 <= Node.val <= 100  
1 <= n <= sz  
 

Follow up: Could you do this in one pass?  

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        ptr = head
        length = 0
        while ptr:
            length+=1
            ptr = ptr.next
        if length == n:
            head = head.next
            return head
        ptr = head
        el_index = length - n
        count = 1
        while ptr:
            if count == el_index:
                if count == length-1:
                    ptr.next = None
                    return head
                else:
                    ptr.next = ptr.next.next
                    return head
            ptr = ptr.next
            count += 1 
```