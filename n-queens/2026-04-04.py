class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        running_arr = []
        col = set()
        pos = set()
        neg = set()

        def dfs(r):
            if r >= n:
                res.append(running_arr[::])
                return

            for i in range(n):
                if i in col or r + i in pos or r - i in neg:
                    continue
                col.add(i)
                pos.add(r + i)
                neg.add(r - i)
                running_arr.append("".join(["." * i] + ["Q"] + ["." * (n - i - 1)]))
                dfs(r + 1)
                col.remove(i)
                pos.remove(r + i)
                neg.remove(r - i)
                running_arr.pop()

        dfs(0)
        return res
