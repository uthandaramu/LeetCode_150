### 173. Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.  
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.  
int next() Moves the pointer to the right, then returns the number at the pointer.  
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.  

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

**Example 1:**  

<img src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" alt="Alt text" width="200"/>

**Input**  
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]  
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]  

**Output**  
[null, 3, 7, true, 9, true, 15, true, 20, false]  

**Explanation**

BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);  
bSTIterator.next();    // return 3  
bSTIterator.next();    // return 7  
bSTIterator.hasNext(); // return True  
bSTIterator.next();    // return 9  
bSTIterator.hasNext(); // return True  
bSTIterator.next();    // return 15  
bSTIterator.hasNext(); // return True  
bSTIterator.next();    // return 20  
bSTIterator.hasNext(); // return False  
 

**Constraints:**

The number of nodes in the tree is in the range [1, 105].  
0 <= Node.val <= 106  
At most 105 calls will be made to hasNext, and next.

**Follow up:**

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

### Without Array (Using Stack)

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        top_element = self.stack.pop()
        out_val = top_element.val
        if top_element.right:
            top_element = top_element.right
            while top_element:
                self.stack.append(top_element)
                top_element = top_element.left
        return out_val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
### With Array (In order Traversal)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.tree_arr = self.lastNode(root)
        self.size = len(self.tree_arr)
        self.ptr = 0

    def next(self):
        """
        :rtype: int
        """
        out = self.tree_arr[self.ptr].val
        self.ptr += 1
        return out
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ptr < self.size:
            return True
        else:
            return False
    
    def lastNode(self, root):
        tree_arr = []
        if root.left:
            tree_arr+=(self.lastNode(root.left))
        tree_arr.append(root)
        if root.right:
            tree_arr+=(self.lastNode(root.right))
        return tree_arr
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```