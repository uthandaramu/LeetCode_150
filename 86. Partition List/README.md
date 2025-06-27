### 86. Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" width="400">

Input: head = [1,4,3,2,5,2], x = 3  
Output: [1,2,2,4,3,5]

**Example 2:**

Input: head = [2,1], x = 2  
Output: [1,2]
 

**Constraints:**

* The number of nodes in the list is in the range [0, 200].
* -100 <= Node.val <= 100
* -200 <= x <= 200

### Own way (bit complex)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        dummy_node = ListNode(-1, head)
        cur_ptr = head
        less_prev = high_prev = dummy_node

        first_high = None

        while cur_ptr:
            if cur_ptr.val < x:
                less_prev.next = cur_ptr
                less_prev = cur_ptr
            else:
                if not first_high:
                    first_high = cur_ptr
                    high_prev = first_high
                else:
                    high_prev.next = cur_ptr
                    high_prev = cur_ptr
            
            cur_ptr = cur_ptr.next
            
        
        less_prev.next = first_high
        if first_high: 
            high_prev.next = cur_ptr
     
        return dummy_node.next
```

### Simple and readable way

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        left_node = left_ptr = ListNode(0)
        right_node = right_ptr = ListNode(0)

        while head:
            if head.val < x:
                left_node.next = head
                left_node = left_node.next
            else:
                right_node.next = head
                right_node = right_node.next
            
            head = head.next
        
        right_node.next = None
        left_node.next = right_ptr.next

        return left_ptr.next
```