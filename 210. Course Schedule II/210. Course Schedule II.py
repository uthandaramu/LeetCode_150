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

            if path_visited[node] == 1:  # Visiting the same node again in the same path
                return False

            if visited[node] == 1:  # Already explored node
                return True

            path_visited[node] = 1
            visited[node] = 1

            for neighbour in neighbourNodes[node]:
                if visited[neighbour] == 0 or path_visited[neighbour] == 1:
                    if not topoSort(neighbour):
                        return False

            stack_box.appendleft(node)  # Storing the edge nodes
            path_visited[
                node] = 0  # Unmarking the node as not visited in path, as it may be visited in different path again

            return True

        for i in range(numCourses):

            if visited[i] == 0:
                x = topoSort(i)

            if not x:
                return []

        return (list(stack_box))