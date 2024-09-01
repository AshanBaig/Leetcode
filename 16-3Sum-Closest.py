class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==target:
                    return target
                if abs(nums[i]+nums[left]+nums[right]-target)<abs(mini-target):
                    mini=nums[i]+nums[left]+nums[right]
                if nums[i]+nums[left]+nums[right]<target:
                    left+=1
                else :
                    right-=1
        return mini
                
