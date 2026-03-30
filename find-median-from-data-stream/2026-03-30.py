class MedianFinder:
    def __init__(self):
        self.lower = []  # max heap
        self.upper = []  # min heap

    def addNum(self, num: int) -> None:
        if len(self.upper) == 0 or num < self.upper[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        diff = len(self.upper) - len(self.lower)

        if diff > 1:
            # upper has too much
            shifted = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -shifted)
        elif diff < 0:
            # lower has too much
            shifted = heapq.heappop(self.lower)
            heapq.heappush(self.upper, -shifted)

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            # even
            return (-self.lower[0] + self.upper[0]) / 2

        return self.upper[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
