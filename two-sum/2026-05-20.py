class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # complement: original idx

        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                return [i, d[num]]

            complement = target - num
            d[complement] = i

        return []
