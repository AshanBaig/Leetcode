import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        if len(piles)==h:
            return max(piles)
        elif len(piles)+1==h:
            temp_l=piles[::-1]
            temp_l.sort()
            return temp_l[-2]
        hour=0
        for banana_eat in range(1,max(piles)+1):
            hour=0
            for j in piles:
                hour+=math.ceil(j/banana_eat)
            if hour==h:
                return banana_eat

s=Solution()
print(s.minEatingSpeed(piles = [312884470],h=312884469))