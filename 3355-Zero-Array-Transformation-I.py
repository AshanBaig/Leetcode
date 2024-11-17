class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)+1
        arr=[0]*n
        for l,r in queries:
             arr[l]+=1
             arr[r+1]-=1
        prefix_sum=[0]*(n+1)
        for i in range(len(arr)):
            prefix_sum[i+1]=prefix_sum[i]+arr[i]
        for i in range(n-1):
            if nums[i]>prefix_sum[i+1]:
                return False
        return True

