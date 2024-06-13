class Solution:
    def heightChecker(self, heights) -> int:
        sort_h=heights[::-1]
        sort_h.sort()
        count=0
        for i in range(len(heights)):
            if heights[i]!=sort_h[i]:
                count+=1
        return count
        