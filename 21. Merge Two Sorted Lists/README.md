### 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.  

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.  

Return the head of the merged linked list.  

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" alt="Alt text" width="200"/>

Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]

**Example 2:**

Input: list1 = [], list2 = []  
Output: []

**Example 3:**

Input: list1 = [], list2 = [0]  
Output: [0]  

**Constraints:**

The number of nodes in both lists is in the range [0, 50].  
-100 <= Node.val <= 100  
Both list1 and list2 are sorted in non-decreasing order.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2
        dummy_node = out_ll = ListNode(-1)
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val < ptr2.val:
                    dummy_node.next = ptr1
                    ptr1 = ptr1.next
                else:
                    dummy_node.next = ptr2
                    ptr2 = ptr2.next

                dummy_node = dummy_node.next
            elif ptr1:
                dummy_node.next = ptr1
                ptr1 = None
            elif ptr2:
                dummy_node.next = ptr2
                ptr2 = None
        
        return out_ll.next
```