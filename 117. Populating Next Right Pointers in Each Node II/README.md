### 117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {  
  int val;  
  Node *left;  
  Node *right;  
  Node *next;  
}  

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" width="400">

Input: root = [1,2,3,4,5,null,7]  
Output: [1,#,2,3,#,4,5,7,#]  
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

**Example 2:**

Input: root = []  
Output: []

**Constraints:**

The number of nodes in the tree is in the range [0, 6000].  
-100 <= Node.val <= 100

**Follow-up:**

* You may only use constant extra space.  
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

###  Depth First search approach (not optimal as per follow up)

```python
from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
            
        storage_stack = deque()
        storage_stack.append(root)

        while storage_stack:
            prev_node = None
            for _ in range(len(storage_stack)):
                node = storage_stack.popleft()

                if prev_node:
                    prev_node.next = node
                prev_node = node

                if node.left:
                    storage_stack.append(node.left)
                if node.right:
                    storage_stack.append(node.right)
        
        return root
```

### Space Optimized optimal as followup question

```python
from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = root

        while head:
            dummy_node = Node(0)
            temp = dummy_node
            while head:
                if head.left:
                    temp.next = head.left
                    temp = temp.next
                if head.right:
                    temp.next = head.right
                    temp = temp.next
            
                head = head.next
            
            head = dummy_node.next
        
        return root
```