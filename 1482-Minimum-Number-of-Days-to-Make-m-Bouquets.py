class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        from math import inf
        low =min(bloomDay)
        high=max(bloomDay)
        ans=-1
        def count_bouquets(mid):
            count=0
            b_count=0
            for b in bloomDay:
                if b<=mid:
                    count+=1
                else:
                    b_count+=int(count/k)
                    count=0
            b_count+=int(count/k)
            return b_count
        while low <=high:
            mid=(low+high)//2
            b_count=count_bouquets(mid)
            if b_count>=m:
                if ans!=-1 or ans<mid:
                    ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans