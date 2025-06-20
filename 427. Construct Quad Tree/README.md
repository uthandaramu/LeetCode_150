### 427. Construct Quad Tree

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.

```
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```
We can construct a Quad-Tree from a two-dimensional area using the following steps:

1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.

<img src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" width="500">

If you want to know more about the Quad-Tree, you can refer to the wiki.

**Quad-Tree format:**

You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.


**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/02/11/grid1.png" width="500">

**Input:** grid = [[0,1],[1,0]]  

**Output:** [[0,1],[1,0],[1,1],[1,1],[1,0]]  

**Explanation:** The explanation of this example is shown below:  
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

<img src="https://assets.leetcode.com/uploads/2020/02/12/e1tree.png" width="500">

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" width="550">

**Input:** grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]  

**Output:** [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]  

**Explanation:** All values in the grid are not the same. We divide the grid into four sub-grids.  
The topLeft, bottomLeft and bottomRight each has the same value.  
The topRight have different values so we divide it into 4 sub-grids where each has the same value.  

**Explanation is shown in the photo below:**  

<img src="https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" width="550">

**Constraints:**

* n == grid.length == grid[i].length
* n == 2x where 0 <= x <= 6

```python
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    #Check if it is a valid Grid
    def isValidGrid(self, row_id, col_id, n):
        val = self.grid[row_id][col_id]

        for i in range(row_id, row_id + n):
            for j in range(col_id, col_id + n):
                if self.grid[i][j] != val:
                    return False
        
        return True

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.grid = grid
        row = col = n = len(grid)

        row_id, col_id = 0, 0

        def rec_grid(row_id, col_id, n):

            if n == 1:
                val = True if self.grid[row_id][col_id] else False
                return Node(val, True)

            if self.isValidGrid(row_id, col_id, n):
                val = True if self.grid[row_id][col_id] else False
                node = Node(val, True)
                return node
            
            else:
                node = Node(True)

                #Top Left
                node.topLeft = rec_grid(row_id, col_id, n//2)

                #Top Right
                node.topRight = rec_grid(row_id, col_id + n//2, n//2)

                #Bottom Left
                node.bottomLeft = rec_grid(row_id + n//2, col_id, n//2)

                #Bottom Right
                node.bottomRight = rec_grid(row_id + n//2, col_id + n//2, n//2)

            return node
        
        x = rec_grid(0, 0, n)
        return x
```