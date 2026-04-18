class Solution:
    def lin_rob(self, nums):
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        a = self.lin_rob(nums[0 : n - 1])
        b = self.lin_rob(nums[1:])

        return max(a, b)
