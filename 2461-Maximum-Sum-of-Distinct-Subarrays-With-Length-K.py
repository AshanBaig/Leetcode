class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        total=0
        ans=0
        for i in range(k):
            d[nums[i]]=d.get(nums[i],0)+1
            total+=nums[i]
        if len(d)==k:
            ans=total
        l=0
        for i in range(k,len(nums)):
           
            d[nums[l]]-=1
            total-=nums[l]
            if d[nums[l]]==0:
                del d[nums[l]]
            l+=1
            d[nums[i]]=d.get(nums[i],0)+1
            total+=nums[i]
            if len(d)==k:
                ans=max(ans,total)
        return ans
        
        