class Solution:
    def searchRange(self, nums, target):
        l=[-1,-1]
        if target not in nums :
            return l
        l[0]=nums.index(target)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                return [l[0],i]
        