### 210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.  
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]  
**Output:** [0,1]  
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

**Example 2:**

**Input:** numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]  
**Output:** [0,2,1,3]  
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.  
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

**Example 3:**

**Input:** numCourses = 1, prerequisites = []  
**Output**: [0]

**Constraints:**

* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= numCourses * (numCourses - 1)
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* ai != bi
* All the pairs [ai, bi] are distinct.

```python
from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        neighbourNodes = defaultdict(list)

        for element in prerequisites:
            neighbourNodes[element[1]].append(element[0])

        visited = [0] * numCourses
        path_visited = visited[:]

        stack_box = deque()
        
        def topoSort(node):

            if path_visited[node] == 1: #Visiting the same node again in the same path
                return False
            
            if visited[node] == 1:  #Already explored node
                return True
            
            path_visited[node] = 1
            visited[node] = 1

            for neighbour in neighbourNodes[node]:
                if visited[neighbour] == 0 or path_visited[neighbour] == 1:
                    if not topoSort(neighbour):
                        return False
            
            stack_box.appendleft(node) #Storing the edge nodes
            path_visited[node] = 0 #Unmarking the node as not visited in path, as it may be visited in different path again

            return True
        
        for i in range(numCourses):
            
            if visited[i] == 0:
                x = topoSort(i)

            if not x:
                return []

        return (list(stack_box))
```