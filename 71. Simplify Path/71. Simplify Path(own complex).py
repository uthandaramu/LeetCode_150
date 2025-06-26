from collections import deque


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = deque()
        size = len(path)

        i, cur_path = 0, ""

        while i < size:

            if path[i] == "/":
                while i < size and path[i] == "/":
                    i = i + 1

                if i < size:

                    if path[i] == ".":
                        while i < size and path[i] != "/":
                            cur_path += path[i]
                            i += 1
                        i -= 1

                        if cur_path == "..":
                            if path_stack:
                                path_stack.pop()

                        elif cur_path != ".":
                            path_stack.append("/" + cur_path)

                        cur_path = ""

                    else:
                        while i < size and path[i] != "/":
                            cur_path += path[i]
                            i += 1
                        i -= 1
                        path_stack.append("/" + cur_path)
                        cur_path = ""

            i += 1

        return "".join(list(path_stack)) if path_stack else "/"