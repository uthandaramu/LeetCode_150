### 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" width="300">

Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" width="100">

Input: head = [1,2]  
Output: [2,1]

**Example 3:**

Input: head = []  
Output: []
 

**Constraints:**

* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        prev_node = None
        while head:
            cur_node = ListNode(head.val)
            cur_node.next = prev_node
            prev_node = cur_node

            head = head.next

        return prev_node
```