class MedianFinder:
    def __init__(self):
        self.lower = []  # maxheap, need to negate values
        self.upper = []  # minheap

    def addNum(self, num: int) -> None:
        if len(self.upper) == 0 or num <= self.upper[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        diff = len(self.upper) - len(self.lower)
        if diff > 1:
            # upper has too much
            shifted = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -shifted)
        elif diff < 0:
            shifted = heapq.heappop(self.lower)
            heapq.heappush(self.upper, -shifted)

    def findMedian(self) -> float:
        if len(self.upper) != len(self.lower):
            return self.upper[0]

        return (self.upper[0] + -self.lower[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
