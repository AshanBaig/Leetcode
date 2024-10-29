class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        def f(count,r,c):
            if r>=row or c>=col:
                return count
            if dp[r][c]!=-1:
                return dp[r][c]
            max_count=count
            if c+1<col and  r-1>-1 and grid[r][c]<grid[r-1][c+1]:
                max_count=max(max_count,f(count+1,r-1,c+1))
            if c+1<col  and grid[r][c]<grid[r][c+1]:
                max_count = max(max_count,f(count+1,r,c+1 ))
            if c+1<col  and  r+1<row and grid[r][c]<grid[r+1][c+1]:
                max_count=max(max_count,f(count+1,r+1,c+1))
            dp[r][c]=max_count
            return dp[r][c]
        ans=0
        dp=[[-1]*col for i in grid]
        for i in range(row):
            ans=max(ans,f(0,i,0))
        return ans
