import random


class RandomizedSet(object):

    def __init__(self):
        self.rand_hash = {}
        self.rand_arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.rand_hash:
            self.rand_hash[val] = len(self.rand_arr)
            self.rand_arr.append(val)
            return True

        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rand_hash:
            idx_to_remove = self.rand_hash[val]
            last_element = self.rand_arr[-1]

            self.rand_hash[last_element] = idx_to_remove

            self.rand_arr[-1], self.rand_arr[idx_to_remove] = self.rand_arr[idx_to_remove], self.rand_arr[-1]

            self.rand_hash.pop(val)
            self.rand_arr.pop()

            return True

        return False

    def getRandom(self):
        """
        :rtype: int
        """
        size = len(self.rand_arr)
        idx = random.randrange(size)
        return self.rand_arr[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()