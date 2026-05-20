class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)

        l = 0
        r = N - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r] and nums[m] > nums[l]:
                return nums[l]

            if nums[m] > nums[r] and nums[m] >= nums[l]:
                # m in left partition
                l = m + 1
            else:
                # m in right partition
                r = m

        return nums[l]
