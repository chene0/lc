class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0

        for num in s:
            if (num - 1) in s:
                continue

            r = num + 1
            while r in s:
                r += 1
            res = max(res, r - num)

        return res
