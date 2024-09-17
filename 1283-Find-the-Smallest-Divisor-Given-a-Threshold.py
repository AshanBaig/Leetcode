class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        from math import ceil
        low=1
        high=max(nums)
        ans=max(nums)
        while low<=high:
            mid=(low+high)//2
            total=0
            for n in nums:
                total+=ceil(n/mid)
            if total<=threshold :
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans    