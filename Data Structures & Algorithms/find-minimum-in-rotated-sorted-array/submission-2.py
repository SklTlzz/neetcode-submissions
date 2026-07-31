class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_value = nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

            min_value = min(min_value, nums[mid])
            
        return min_value
