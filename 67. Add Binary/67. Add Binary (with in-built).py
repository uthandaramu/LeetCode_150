class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)

        c = bin(a + b)  #bin() returs "0b"+ <eqivalent binary string>

        return c[2:] #Trimming "0b"