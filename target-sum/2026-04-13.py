class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p + n = total
        # p - n = target
        # p = (total + target) / 2

        total = 0
        for num in nums:
            total += num

        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        p = (total + target) // 2
        dp = [1] + [0] * p

        for num in nums:
            for t in range(p, num - 1, -1):
                dp[t] = dp[t] + dp[t - num]

        return dp[p]
