class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        storage = []
        def rec_fun(openN, closeN):
            if openN == closeN == n :
                out.append("".join(storage))
                return

            if openN < n:
                storage.append("(")
                rec_fun(openN+1, closeN)
                storage.pop()

            if closeN < openN:
                storage.append(")")
                rec_fun(openN, closeN+1)
                storage.pop()

        rec_fun(0,0)
        return (out)