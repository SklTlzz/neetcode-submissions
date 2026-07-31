class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        l = 1
        r = len(nums) - 1
        min_value = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if nums[mid - 1] < nums[mid]:
                if nums[mid] > nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]

            min_value = min(min_value, nums[mid])

        return min_value
