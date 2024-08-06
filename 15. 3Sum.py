class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # Duplicate triplets ko avoid karne ke liye
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    chunk=[nums[i],nums[l],nums[r]]
                    lst.append(chunk)
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return lst