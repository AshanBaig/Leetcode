class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_r=triangle[-1]
        for r in range(len(triangle)-2,-1,-1): #not taking last row
            curr_r=[]
            for c in range(len(triangle[r])-1,-1,-1): #we have to take all columns of 2nd last row
                down=triangle[r][c]+prev_r[c]
                diagonal=triangle[r][c]+prev_r[c+1]
                curr_r.append(min(down,diagonal))
            prev_r=curr_r[::-1]
        return prev_r[0]
        