### 399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

**Example 1:**

**Input:** equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]  
**Output:** [6.00000,0.50000,-1.00000,1.00000,-1.00000]  
**Explanation:**  
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

**Example 2:**

**Input:** equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]  
**Output:** [3.75000,0.40000,5.00000,0.20000]

**Example 3:**

**Input:** equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]  
**Output:** [0.50000,2.00000,-1.00000,-1.00000]
 
**Constraints:**

* 1 <= equations.length <= 20
* equations[i].length == 2
* 1 <= Ai.length, Bi.length <= 5
* values.length == equations.length
* 0.0 < values[i] <= 20.0
* 1 <= queries.length <= 20
* queries[i].length == 2
* 1 <= Cj.length, Dj.length <= 5
* Ai, Bi, Cj, Dj consist of lower case English letters and digits.


```python
from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        #Intiuation: weighted graph approach will be used.

        neighbourNodes = defaultdict(list)

        #Eg: a : [b, 2.0]
        #same combo, b : [a, 1/2.0] <bidirectional>
        for val, equ in enumerate(equations):
            equ1, equ2 = equ
            neighbourNodes[equ1].append([equ2, values[val]])
            neighbourNodes[equ2].append([equ1, 1/values[val]])
        

        def evaluate(node):

            if node[0] not in neighbourNodes or node[1] not in neighbourNodes:
                return -1.0

            visited = set()
            result = 1
            bfsQ = deque()
            bfsQ.append((node[0], 1))
            visited.add(node[0])

            while bfsQ:
                cur_node, weight = bfsQ.popleft()

                if cur_node == node[1]:
                    return weight

                for neighbours in neighbourNodes[cur_node]:
                    nextNode, nextWeight = neighbours

                    # will be multiplying the results as I traverse 
                    if nextNode not in visited:
                        bfsQ.append((nextNode, weight * nextWeight))
                        visited.add(nextNode)
                    
            return -1

        result = []
        for query in queries:
            result.append(evaluate(query))

        return (result)
```