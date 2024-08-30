class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        len_list=len(nums)
        for i in set(nums):
            while nums.count(i)>2:
                nums.remove(i)
                count+=1
        nums+=['_']*count
        return len_list-count            
        