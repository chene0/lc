class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalpost = 0

        for i in range(len(nums)):
            if i > goalpost:
                return False

            goalpost = max(goalpost, nums[i] + i)

        return True
