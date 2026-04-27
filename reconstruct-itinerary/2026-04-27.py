class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for a, b in tickets:
            heapq.heappush(adj[a], b)

        res = []

        def dfs(a):
            while adj[a]:
                b = heapq.heappop(adj[a])
                dfs(b)

            res.append(a)

        dfs("JFK")
        return res[::-1]
