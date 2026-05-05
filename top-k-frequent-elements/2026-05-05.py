class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)

        for num in nums:
            freq[num] += 1

        pq = []  # (freq, num)

        for num in freq:
            heapq.heappush(pq, (-freq[num], num))

        res = []
        for i in range(k):
            if not pq:
                break
            f, num = heapq.heappop(pq)
            res.append(num)

        return res
