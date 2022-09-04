class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return any(target in row for row in matrix)
