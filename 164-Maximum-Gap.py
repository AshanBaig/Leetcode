class Solution:
    from math import inf
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi=-inf
        if len(nums)<2:
            return 0
        for i in range(len(nums)-1):
            maxi=max(maxi,nums[i+1]-nums[i])
        return maxi