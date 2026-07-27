class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []

        for arr in matrix:
            flat_matrix += arr

        l = 0
        r = len(flat_matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if flat_matrix[mid] == target:
                return True
            elif flat_matrix[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
