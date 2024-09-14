class Solution:
    from math import ceil,inf
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=inf
        while low<=high:
            mid=(low+high)//2
            total=0
            for b in piles:
                total+=ceil(b/mid)
                if total>h:
                    low=mid+1
                    break
            if total<=h:
                ans=min(ans,mid)
                high=mid-1
        return ans