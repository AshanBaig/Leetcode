class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        row=0
        col=0
        while len(ans)!=len(mat)*(len(mat[0])):
            while row>=0 and col<len(mat[0]):
                    ans.append(mat[row][col])
                    row-=1
                    col+=1
            if row<0 and col>=len(mat[0]):
                row=1
                col=len(mat[0])-1
            elif row<0:
                row=0
            elif col>=len(mat[0]):
                col-=1
                row+=2
            if len(ans)==len(mat)*(len(mat[0])):
                break
            while row<len(mat) and col>-1:
                ans.append(mat[row][col])
                row+=1
                col-=1
            if col<0 and row>=len(mat):
                col=1
                row=len(mat)-1
            elif row>=len(mat):
                col+=2
                row=len(mat)-1
            elif col<0:
                col=0
        return ans
        
                