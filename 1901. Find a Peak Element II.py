class Solution:
    def findPeakGrid(self, mat) :
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j-1>=0 and mat[i][j]<mat[i][j-1]:  #left check False
                    pass
                elif j+1<len(mat[i]) and mat[i][j]<mat[i][j+1]:
                    pass
                     #right check if false so mat[i][j] is greateer
                elif i-1>=0 and mat[i][j]<mat[i-1][j]:
                    pass
                elif i+1<len(mat) and mat[i][j]<mat[i+1][j]:
                    pass
                else:
                    return [i,j]