class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort = nums[0]
        hare = nums[nums[0]]

        while tort != hare:
            tort = nums[tort]
            hare = nums[nums[hare]]

        anchor = 0
        while anchor != tort:
            anchor = nums[anchor]
            tort = nums[tort]

        return anchor
