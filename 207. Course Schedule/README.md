### 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.  
Return true if you can finish all courses. Otherwise, return false.

**Example 1:**

Input: numCourses = 2, prerequisites = [[1,0]]  
Output: true  
Explanation: There are a total of 2 courses to take.   
To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]  
Output: false  
Explanation: There are a total of 2 courses to take.   
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

**Constraints:**

* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= 5000
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* All the pairs prerequisites[i] are unique.

### DFS Approach

```python
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        neighbour_nodes = defaultdict(list)

        for element in prerequisites:
            neighbour_nodes[element[0]].append(element[1])

        visited = [0] * numCourses
        
        #DFS approach
        def isValidPath(node):

            if visited[node] == 1:  # Visiting Node visiting itself again
                return False

            if visited[node] == 2:  # Already Explored path
                return True

            visited[node] = 1  # marking the cur_node as currently visiting

            for neighbour in neighbour_nodes[node]:
                if not isValidPath(neighbour):
                    return False
            visited[node] = 2 #marking the current node as visited

            return True

        for i in range(numCourses):
            if not isValidPath(i):
                return False

        return True
```