class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_max=-10**4
        overall_max=-10**4
        for i in nums:
            cur_max=max(cur_max+i,i)
            overall_max=max(cur_max,overall_max)
        return overall_max