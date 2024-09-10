class Solution:
    def findMin(self, nums: List[int]) -> int:
        from math import inf
        def binary_search_rotated(low=0,high=len(nums)-1):
            ans=inf
            while low<=high:
                mid=(low+high)//2
                if nums[low]<=nums[high]:
                    return min(ans,nums[low])
                if nums[mid]<ans:
                    ans=nums[mid]
                if nums[low]<=nums[mid]: #left sorted
                    if nums[low]<ans:
                        ans=nums[low] 
                    low=mid+1
                    continue
                else:
                    ans=min(ans,nums[mid])
                    high=mid-1
            return ans
        return binary_search_rotated()