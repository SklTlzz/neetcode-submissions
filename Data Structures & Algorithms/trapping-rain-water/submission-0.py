class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        cumulative_area = 0
        max_left_stack = []
        max_right_stack = []

        for h in height:
            max_h = max(h, max_left_stack[-1] if max_left_stack else h)
            max_left_stack.append(max_h)

        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            max_h = max(h, max_right_stack[-1] if max_right_stack else h)
            max_right_stack.append(max_h)

        max_right_stack = max_right_stack[::-1]

        for i, value in enumerate(height):
            cumulative_area += (min(max_left_stack[i], max_right_stack[i]) - value)

        return cumulative_area
