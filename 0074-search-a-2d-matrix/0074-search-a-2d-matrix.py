class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        found_row = -1
        while t <= b:
            mid = t + ((b - t) // 2)
            if target > matrix[mid][len(matrix[0]) - 1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                found_row = mid
                break
        
        if found_row == -1:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[found_row][mid] > target:
                r = mid - 1
            elif matrix[found_row][mid] < target:
                l = mid + 1
            else:
                return True
        return False