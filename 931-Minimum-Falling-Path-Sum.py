class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        prev_r=matrix[0]
        # for start in range(len(matrix[0])): #start from 1st row and every column one by one
        for r in range(1,len(matrix)):
                curr_r=[]
                for c in range(0,len(matrix[0])):
                    #base case
                    l_dg,r_dg=10**4,10**4
                    if c>0:
                        l_dg=matrix[r][c]+prev_r[c-1]
                    if c+1<len(matrix):
                        r_dg=matrix[r][c]+prev_r[c+1]
                    straight=matrix[r][c]+prev_r[c]
                    curr_r.append(min(l_dg,r_dg,straight))
                prev_r=curr_r
        return min(prev_r)