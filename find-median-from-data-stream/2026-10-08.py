import heapq


class MedianFinder:
    def __init__(self):
        self.less = []
        self.greater = []

    def addNum(self, num: int) -> None:
        if len(self.greater) == 0 or num >= self.greater[0]:
            heapq.heappush(self.greater, num)
        else:
            heapq.heappush(self.less, -num)

        size_diff = len(self.greater) - len(self.less)  # maintain 1 or 0

        if size_diff > 1:
            # transfer one to less
            heapq.heappush(self.less, -heapq.heappop(self.greater))
        elif size_diff < 0:
            # transfer one to greater
            heapq.heappush(self.greater, -heapq.heappop(self.less))

    def findMedian(self) -> float:
        if len(self.greater) == len(self.less):
            # even list size
            return (self.greater[0] - self.less[0]) / 2

        return self.greater[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
