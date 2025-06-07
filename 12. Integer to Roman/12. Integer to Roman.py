class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = [
            [1, 'I'],
            [4, 'IV'],
            [5, "V"],
            [9, 'IX'],
            [10, "X"],
            [40, "XL"],
            [50, "L"],
            [90, "XC"],
            [100, "C"],
            [400, "CD"],
            [500, "D"],
            [900, "CM"],
            [1000, "M"]
        ]

        out_str = ""

        for val, sym in reversed(roman_dict):
            if num >= val:
                times = num // val
                out_str += times * sym
                num = num % val

        return (out_str)