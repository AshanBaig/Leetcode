class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        k=k%len(nums)
        d={}
        pos=0
        for i in range(len(nums)):
            if i+k>=len(nums):
                d[pos]=nums[i]
                pos+=1
            else:
                d[i+k]=nums[i]
        for i in d:
            nums[i]=d[i]