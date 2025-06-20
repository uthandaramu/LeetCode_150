### 82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" width="300">

Input: head = [1,2,3,3,4,4,5]  
Output: [1,2,5]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" width="300">

Input: head = [1,1,1,2,3]  
Output: [2,3]

**Constraints:**

* The number of nodes in the list is in the range [0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        dummy_node = ListNode(0, head)
        prev = dummy_node

        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            
            head = head.next
        
        return dummy_node.next
```