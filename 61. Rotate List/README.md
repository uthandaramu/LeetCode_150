### 61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" width="250">

Input: head = [1,2,3,4,5], k = 2  
Output: [4,5,1,2,3]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" width="200">

Input: head = [0,1,2], k = 4  
Output: [2,0,1]

**Constraints:**

* The number of nodes in the list is in the range [0, 500].
* -100 <= Node.val <= 100
* 0 <= k <= 2 * 109

### Own Approach (complex and extra space)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        nodeIdx = {}

        count = 0

        ptr = out_ptr = head

        while ptr:
            nodeIdx[count] = ptr
            ptr= ptr.next
            count += 1
        
        rotate_num = k % count

        rotateNode = nodeIdx[count - rotate_num - 1]

        if rotateNode.next:
            tempNext = out_ptr = rotateNode.next
            rotateNode.next = None
            while tempNext.next:
                tempNext = tempNext.next
        
            tempNext.next = head
        
        return out_ptr
```

### Without extra space (optimized)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
            
        length = count = 0
        ptr = head

        while ptr:
            tail = ptr
            length += 1
            ptr = ptr.next
        
        tail.next = head

        idxToRotate = length - (k % length)

        ptr = head
        start = None
        while count <= idxToRotate - 1:
            count += 1
            start = ptr
            ptr = ptr.next

        if start:
            head = start.next
            start.next = None

        return head
```