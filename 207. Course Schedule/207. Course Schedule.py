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