from collections import deque


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_val = i = 0
        sign_val = 1
        res = 0
        stack_box = deque()
        size = len(s)

        while i < size:
            if s[i].isdigit():
                while i < size and s[i].isdigit():
                    cur_val = cur_val * 10 + int(s[i])
                    i += 1
                i -= 1

                res += (cur_val * sign_val)
                sign_val = 1
                cur_val = 0

            elif s[i] == "+":
                sign_val = 1

            elif s[i] == "-":
                sign_val = -1

            elif s[i] == "(":
                stack_box.append(res)
                stack_box.append(sign_val)
                cur_val = 0
                sign_val = 1
                res = 0

            elif s[i] == ")":
                prev_sign = stack_box.pop()
                prev_res = stack_box.pop()
                res *= prev_sign
                res += prev_res

            i += 1

        return res