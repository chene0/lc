class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p + n == total
        # p - n == target
        # p = (total + target) / 2

        total = 0
        for num in nums:
            total += num

        if total + target < 0 or (total + target) % 2 != 0:
            return 0

        p = (total + target) // 2
        sum_counts = [1] + [0] * p

        for num in nums:
            for i in range(p, num - 1, -1):
                sum_counts[i] += sum_counts[i - num]

        return sum_counts[p]
