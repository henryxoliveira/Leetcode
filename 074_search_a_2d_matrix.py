from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            value = matrix[r][c]

            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

