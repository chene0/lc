class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        running_arr = []
        running_sum = 0

        def backtrack(idx):
            nonlocal running_sum
            if running_sum == target:
                res.append(running_arr[::])
                return

            if running_sum > target or idx >= len(candidates):
                return

            candidate = candidates[idx]
            running_arr.append(candidate)
            running_sum += candidate
            backtrack(idx + 1)
            running_arr.pop()
            running_sum -= candidate

            i = idx
            while (i + 1) < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
