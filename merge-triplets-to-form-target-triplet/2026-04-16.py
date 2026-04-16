class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = [False, False, False]

        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            for i in range(3):
                if triplet[i] == target[i] and not a[i]:
                    a[i] = True

            if all(a):
                return True

        return all(a)
