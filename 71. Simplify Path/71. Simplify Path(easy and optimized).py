from collections import deque


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split("/")

        path_stack = deque()

        for cur_path in path_list:

            if cur_path == "" or cur_path == ".":
                continue

            elif cur_path == "..":
                if path_stack:
                    path_stack.pop()

            else:
                path_stack.append("/" + cur_path)

        return "".join(path_stack) if path_stack else "/"