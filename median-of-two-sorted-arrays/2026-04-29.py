class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        tot = len(A) + len(B)
        half = tot // 2

        l = 0
        r = len(A) - 1

        while True:
            mA = (l + r) // 2
            # (mA+1) + (mB+1) = half
            mB = half - mA - 2

            lA = float("-inf") if mA < 0 else A[mA]
            lB = float("-inf") if mB < 0 else B[mB]
            rA = float("inf") if (mA + 1) >= len(A) else A[mA + 1]
            rB = float("inf") if (mB + 1) >= len(B) else B[mB + 1]

            if lA <= rB and lB <= rA:
                # valid
                if tot % 2 == 0:
                    # even
                    return (max(lA, lB) + min(rA, rB)) / 2
                return min(rA, rB)

            if lA > rB:
                # A mid is too large
                r = mA - 1
            else:
                l = mA + 1

        return -1
