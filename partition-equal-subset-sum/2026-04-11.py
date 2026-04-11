class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        is_even = total % 2 == 0
        if not is_even:
            return False

        half = total / 2

        sums = set([0])

        for num in nums:
            sums_clone = sums.copy()

            for prev_sum in sums:
                new_sum = prev_sum + num
                if new_sum == half:
                    return True
                if new_sum > half:
                    continue
                sums_clone.add(new_sum)

            sums = sums_clone

        return False
