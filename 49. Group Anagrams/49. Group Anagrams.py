class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hash_dict:
                hash_dict[sorted_word] = [word]
            else:
                hash_dict[sorted_word].append(word)

        out = []

        for i in hash_dict.values():
            out.append(i)

        return (out)