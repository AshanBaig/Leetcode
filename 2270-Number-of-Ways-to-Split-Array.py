class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        self.left=nums[0]
        self.right=sum(nums[1:])
        self.count=0
        def f(ind):
            if ind>=len(nums):
                return
            if self.left>=self.right:
                self.count+=1
            print(self.left,self.right,ind)
            self.left+=nums[ind]
            self.right-=nums[ind]
            f(ind+1)
        f(1)
        return self.count

            