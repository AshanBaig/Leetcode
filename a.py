class Solution:
    def permute(self, nums: list[int]) :
        l=[]
        if len(nums)==1:
            return nums
        target=nums
        # factorial
        def factorial(x):
            fact=1
            while x!=0:
                fact*=x
                x-=1
            return fact
        fact=factorial(len(nums))
        l=[]
        count=0
        for i in range(len(nums)):
            first=[nums[i]]
            chunk=nums[:]
            while count<=len(nums)-1:
                if count==0:
                   break
                sub_first=nums[count]
                first.append(sub_first)
            while len[chunk]!=0:
                if first+chunk in l:
                    
                else:
                    
s=Solution()
print(s.permute([0,1]))