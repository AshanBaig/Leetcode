class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        
        left=nums[0]
        count=1
        maxi=1
        for i in range(1,len(nums)):
            if left<nums[i]:
                count+=1
                left=nums[i]
            else:
                maxi=max(count,maxi)
                count=1
            left=nums[i]
        maxi=max(count,maxi)
        return maxi
    