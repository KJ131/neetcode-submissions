class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) -1
        while left <= right:
            middle = (left + right)//2
            ld = matrix[middle][-1]
            fd = matrix[middle][0]
            if ld == target or fd == target: return True
            if target >fd and target <ld:
                break
            if ld < target:
                left = middle + 1
            elif ld > target:
                right = middle - 1
        left = 0
        right = len(matrix[middle])-1
        while left <= right:
            mid = (left + right)//2
            if matrix[middle][mid] == target:
                return True
            if matrix[middle][mid]< target:
                left = mid + 1
            else:
                right = mid - 1 
        return False

        