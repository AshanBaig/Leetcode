class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1=nums[0]
        prev2=0
        for i in range(1,len(nums)):
            take=nums[i]
            if i>1:
                take+=prev2
            nontake=prev1
            curi=max(take,nontake)
            prev2=prev1
            prev1=curi
        return prev1