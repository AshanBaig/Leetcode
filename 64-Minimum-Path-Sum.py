class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==1:
            return sum(grid[0])
        prev_r=[0]*len(grid)
        for i in range(len(grid)):
            curr_r=[0]*len(grid[i])
            for j in range(len(grid[i])):
                if i==0 and j==0:
                    curr_r[j]=grid[i][j]
                    continue
                up,left=10**8,10**8 #bcz upper limit is 200 as discripton
                if i>0:
                    up=prev_r[j]+grid[i][j]
                if j>0:
                    left=curr_r[j-1]+grid[i][j]
                curr_r[j]=min(up,left)
            prev_r=curr_r
        return prev_r[-1]