class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp=[]
        for i in grid:
            chunk1=[]
            for j in range(len(i)):
                chunk2=[]
                for k in range(len(i)):
                    chunk2.append(-1)
                chunk1.append(chunk2)
            dp.append(chunk1)
        for j1 in range(len(grid[-1])):
            for j2 in range(len(grid[-1])):
                if j1==j2:
                    dp[-1][j1][j2]=grid[-1][j1]
                else:
                    dp[-1][j1][j2]=grid[-1][j1]+grid[-1][j2]
        print(dp)
        #now we have 3 states row,col1,col2   col1 and col 2 can be anything from 0 to m-1
        for row in range(len(grid)-2,-1,-1):
            for col1 in range(len(grid[0])):
                for col2 in range(len(grid[0])):
                    move=[-1,0,1]
                    maxi=-10**4
                    for i in move:
                        for j in move:
                            value=0
                            if col1==col2:
                                value=grid[row][col1]
                            else:
                                value=grid[row][col1]+grid[row][col2]
                            if col1+i>=0 and col1+i<len(grid[0]) and col2+j>=0 and col2+j<len(grid[0]):
                                value+=dp[row+1][col1+i][col2+j]
                            maxi=max(maxi,value)
                    dp[row][col1][col2]=maxi
        return dp[0][0][len(grid[0])-1]
# print(dp[0][0][-1])
            