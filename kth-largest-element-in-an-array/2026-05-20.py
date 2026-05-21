class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []  # minheap

        for num in nums:
            if len(pq) >= k and num <= pq[0]:
                continue

            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]
