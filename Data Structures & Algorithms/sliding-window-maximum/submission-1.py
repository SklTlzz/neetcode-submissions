class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        max_window_values = []
        max_stack_l = 0
        max_values_stack = []

        while r != len(nums):
            while max_values_stack and len(max_values_stack) > max_stack_l and nums[max_values_stack[-1]] < nums[r]:
                max_values_stack.pop()

            max_values_stack.append(r)

            if l > max_values_stack[max_stack_l]:
                max_stack_l += 1

            if r - l + 1 == k:
                max_window_values.append(nums[max_values_stack[max_stack_l]])
                l += 1

            r += 1

        return max_window_values
