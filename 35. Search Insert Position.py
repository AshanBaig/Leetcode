class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
                if nums[i]==target:
                    return i
                
        for i in range(len(nums)):
                if i+1<len(nums) and nums[i]<target and nums[i+1]>target:
                    return i+1
                elif nums[-1]<target:
                    return len(nums)
                elif nums[0]>target:
                    return 0
                


        