class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1 :]
                adj[key].append(word)

        pq = [(1, beginWord)]
        visited = set()

        while pq:
            path, word = heapq.heappop(pq)

            if word == endWord:
                return path

            if word in visited:
                continue
            visited.add(word)

            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1 :]
                neighbours = adj[key]
                for neighbour in neighbours:
                    heapq.heappush(pq, (path + 1, neighbour))

        return 0
