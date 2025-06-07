class MedianFinder(object):

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # We have two heaps:- MinHeap to store large values, MaxHeap to store small values
        # By default push the values in small heap
        heapq.heappush(self.small, -num)

        # does small heap always holds lesser values than elements in large heap
        if self.small and self.large and -self.small[0] >= self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # does the size difference of small and large heap don't exceed 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return ((-self.small[0] + self.large[0]) / 2.0)
        elif len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()