class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rec_area = 0
        stack = []

        for i in range(len(heights)):
            h = heights[i]

            while h < (heights[stack[-1]] if stack else 0):
                curr_idx = stack.pop()
                height = heights[curr_idx]
                width = i - (stack[-1] if stack else -1) - 1
                curr_rec_area = height * width

                max_rec_area = max(max_rec_area, curr_rec_area)
            
            stack.append(i)

        while stack:
            curr_idx = stack.pop()
            height = heights[curr_idx]
            width = len(heights) - (stack[-1] if stack else -1) - 1
            curr_rec_area = height * width

            max_rec_area = max(max_rec_area, curr_rec_area)


        return max_rec_area
