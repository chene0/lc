class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        latest = {}

        for i in range(len(s)):
            c = s[i]
            latest[c] = i

        res = []
        goalpost = 0
        runner = 0

        for i in range(len(s)):
            c = s[i]
            goalpost = max(goalpost, latest[c])
            runner += 1

            if i >= goalpost:
                res.append(runner)
                runner = 0

        return res
