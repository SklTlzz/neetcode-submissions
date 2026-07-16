class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #curr_rec_area = 0
        #prev_rec_area = 0
        max_rec_area = 0
        #stack = []

        for curr_idx in range(len(heights)):
            curr_h = heights[curr_idx]
            i = curr_idx
            start = -1
            end = len(heights)

            while i > -1:
                if heights[i] < curr_h:
                    start = i
                    break

                i -= 1

            i = curr_idx

            while i < len(heights):
                if heights[i] < curr_h:
                    end = i
                    break

                i += 1

            curr_rec_area = (end - start - 1) * curr_h
            max_rec_area = max(max_rec_area, curr_rec_area)

        return max_rec_area
