class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = collections.defaultdict(int)

        for card in hand:
            freq[card] += 1

        pq = []
        for card in freq:
            heapq.heappush(pq, card)

        while pq:
            card = heapq.heappop(pq)
            min_freq = freq[card]
            if min_freq == 0:
                continue

            for i in range(groupSize):
                next_card = card + i
                if freq[next_card] < min_freq:
                    return False
                freq[next_card] -= min_freq

        return True
