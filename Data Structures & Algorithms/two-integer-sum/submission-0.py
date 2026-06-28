class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = dict()

        for i, elem in enumerate(nums):
            diff = target - elem

            if diff in prev_nums:
                return [prev_nums[diff], i]
            else:
                prev_nums[elem] = i
