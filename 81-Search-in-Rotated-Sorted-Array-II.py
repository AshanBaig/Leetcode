class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def Search_in_rotatedII(low=0,high=len(nums)-1):
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return True
                if nums[low]==nums[high]==nums[mid]:
                    low=low+1
                    high=high-1
                    continue
                if nums[low]<=nums[mid]: #array is sorted
                    if nums[low]<=target and target<nums[mid] :
                        high=mid-1
                    else:
                        low=mid+1
                else:
                    if nums[mid]<target and target<= nums[high]:
                        low=mid+1   
                    else:
                        high=mid-1
            return False
        return Search_in_rotatedII()