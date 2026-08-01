class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        half = (len(nums1) + len(nums2) + 1) // 2
        l = 0
        r = len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i
            left_A = A[i-1] if i != 0 else float("-inf")
            left_B = B[j-1] if j != 0 else float("-inf")
            right_A = A[i] if i != len(A) else float("inf")
            right_B = B[j] if j != len(B) else float("inf")

            if left_A <= right_B and left_B <= right_A:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left_A, left_B)
                else:
                    return (max(left_A, left_B) + min(right_A, right_B)) / 2
            elif left_A > right_B:
                r = i - 1
            else:
                l = i + 1
