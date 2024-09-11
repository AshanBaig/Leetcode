class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #math concept (even,odd) index before the single element  (odd,even) after single element 
        def single(low=1,high=len(nums)-2):
            if len(nums)==1:
                return nums[0]
            if nums[0]!=nums[1]:
                return nums[0]
            if nums[len(nums)-1]!=nums[len(nums)-2]:
                return nums[-1]
            while low<=high:
                mid=(low+high)//2
                if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                    return nums[mid]
                if mid%2==0: 
                    if nums[mid]==nums[mid+1]:
                        low=mid+1
                    else:
                        high=mid-1
                else:
                    if nums[mid]==nums[mid-1]:
                        low=mid+1
                    else:
                        high=mid-1    
        return single()    
            