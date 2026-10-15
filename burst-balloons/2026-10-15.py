class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        dp = [[0] * len(nums) for _ in range(len(nums))]

        for d in range(2, n + 2):
            for l in range(0, len(nums) - d):
                r = l + d  # inclusive
                for m in range(l + 1, r):
                    curr = nums[l] * nums[m] * nums[r]
                    dp[l][r] = max(dp[l][r], curr + dp[l][m] + dp[m][r])

        return dp[0][len(nums) - 1]
