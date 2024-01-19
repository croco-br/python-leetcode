from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
             return False
    
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
            
        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // n][mid % n]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False

Solution().searchMatrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
)
