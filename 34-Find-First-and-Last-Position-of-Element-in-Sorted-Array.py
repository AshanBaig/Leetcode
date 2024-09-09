class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l=[-1,-1]
        # if target not in nums :
        #     return l
        # l[0]=nums.index(target)
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==target:
        #         return [l[0],i]
        def first_occur(low=0,high=len(nums)-1,first=-1):
            while True:
                if low>high:
                    break
                mid=int((low+high)/2)
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return first
        first_occur()
        def last_occur(low=0,high=len(nums)-1,last=-1):
            while True:
                if low>high:
                    break
                mid=int((low+high)/2)
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return last
        
        return [first_occur(),last_occur()]