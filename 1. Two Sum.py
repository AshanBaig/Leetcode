class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


print(9646324351<2**31)
x=9646324351
if x>=-1*(2**31) and x<=(2**31)-1:
            print('h')