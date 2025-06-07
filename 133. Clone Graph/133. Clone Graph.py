"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        self.visited = {}
        def rec_graph(cur_node):
            if cur_node.val in self.visited:
                return self.visited[cur_node.val]

            copy_node = Node(cur_node.val)
            self.visited[cur_node.val] = copy_node

            for neighbors in cur_node.neighbors:
                copy_node.neighbors.append(rec_graph(neighbors))

            return copy_node

        x = rec_graph(node)
        return x