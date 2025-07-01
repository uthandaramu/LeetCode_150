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