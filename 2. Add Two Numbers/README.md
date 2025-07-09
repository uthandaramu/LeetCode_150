### 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" width="350"> 

Input: l1 = [2,4,3], l2 = [5,6,4]  
Output: [7,0,8]  
Explanation: 342 + 465 = 807.

**Example 2:**

Input: l1 = [0], l2 = [0]  
Output: [0]

**Example 3:**

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]  
Output: [8,9,9,9,0,0,0,1]

**Constraints:**

* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy_node = res_ptr = ListNode(-1)

        while ptr1 or ptr2:
            val1 = 0 if not ptr1 else ptr1.val
            val2 = 0 if not ptr2 else ptr2.val
            res = val1 + val2

            if carry:
                res += carry
                carry = 0

            if res > 9:
                carry = 1
                res = res % 10

            res_ptr.next = ListNode(res)
            res_ptr = res_ptr.next
            if ptr1: ptr1 = ptr1.next
            if ptr2: ptr2 = ptr2.next 
        
        if carry:
            res_ptr.next = ListNode(carry)
        
        return dummy_node.next
```