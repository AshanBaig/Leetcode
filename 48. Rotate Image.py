class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        mat_copy=[i.copy()  for i in matrix]
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                print(mat_copy)
                # print(row,col)
                # print(matrix[row][col],mat_copy[col][row])
                matrix[row][col]=mat_copy[col][row]
        print(matrix)
s=Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))