class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target=len(nums)-1
        if target==0:
            return True
        jump=1
        for i in range(len(nums)-1):
            jump-=1
            if nums[i]==0:
                if jump<=0:
                    print(nums[i])
                    break
                continue
            if i+nums[i]>=target:
                return True
            jump=max(nums[i],jump)
        return False
        