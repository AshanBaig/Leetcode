class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        num_index={}
        for ind,num in enumerate(nums):
            if num in num_index and ind-num_index[num]<=k:
                return True
            num_index[num]=ind
        return False