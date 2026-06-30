class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_arr[i] *= nums[i - 1] * prefix_arr[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] *= nums[i + 1] * suffix_arr[i + 1]

        for i in range(len(prefix_arr)):
            result = prefix_arr[i] * suffix_arr[i]
            output.append(result)

        return output
        