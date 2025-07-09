### 25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" width="400"> 

Input: head = [1,2,3,4,5], k = 2  
Output: [2,1,4,3,5]

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" width="400">

Input: head = [1,2,3,4,5], k = 3  
Output: [3,2,1,4,5]

**Constraints:**

* The number of nodes in the list is n.
* 1 <= k <= n <= 5000
* 0 <= Node.val <= 1000
 

**Follow-up: Can you solve the problem in O(1) extra memory space?**

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        ptr = head
        prev = None
        while ptr:
            tempNext = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tempNext

        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 1: return head
        
        ptr = groupFirst = head
        count = 0

        while ptr:
            count += 1
            if count == k:
                #Taking backup of ptr Next
                ptrNext = ptr.next

                #making this group end points to None
                ptr.next = None

                #reverse the group
                revGroup = self.reverseList(groupFirst)

                #Alter the head for first group
                if groupFirst == head:
                    head = revGroup
                else:
                    #for group other than first, connect with previous group end
                    prevGroupLast.next = revGroup
                
                #remembering previous group end
                prevGroupLast = groupFirst
                count = 0

                #moving to next group
                groupFirst = ptr = ptrNext

            else:
                ptr = ptr.next
            
        if count:
            #if there is still count, joining previous group end and unfinished last group first element
            prevGroupLast.next = groupFirst
        
        return (head)
```