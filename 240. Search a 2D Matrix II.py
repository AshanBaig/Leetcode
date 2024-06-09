class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False
        