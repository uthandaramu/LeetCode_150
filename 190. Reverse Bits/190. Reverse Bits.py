class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            bit = (n >> i) & 1
            out = out | (bit << (31-i))
        return (out)