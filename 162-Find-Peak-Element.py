class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_peak(low=1,high=len(nums)-2):
            if len(nums)==1 or nums[0]>nums[1]:
                return 0
            elif nums[len(nums)-2]<nums[len(nums)-1]:
                return len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid]>nums[mid-1] and nums[mid]< nums[mid+1]:
                    low=mid+1
                else:
                    high=mid-1
        return binary_peak()