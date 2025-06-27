class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        i = 0
        res = cur_val = prev_val = 0
        cur_operator = "+"

        while i < size:

            if s[i].isdigit():
                while i < size and s[i].isdigit():
                    cur_val = cur_val * 10 + int(s[i])
                    i += 1

                i -= 1

                if cur_operator == "+":
                    res += cur_val
                    prev_val = cur_val

                elif cur_operator == "-":
                    res -= cur_val
                    prev_val = -cur_val

                elif cur_operator == "*":
                    res -= prev_val
                    prev_val = cur_val * prev_val
                    res += prev_val

                else:
                    res -= prev_val
                    prev_val = int(float(prev_val) / cur_val)
                    res += prev_val

                cur_val = 0

            elif s[i] != " ":
                cur_operator = s[i]

            i += 1

        return res