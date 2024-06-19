class Solution:
    def maximumProduct(self, nums) -> int:
        n=sorted(nums,reverse=True)
        maxi=n[0]*n[1]*n[2]
        if n[-1]<0 and n[-2]<0:
            maxi=max(n[0]*n[-1]*n[-2],maxi)
        return maxi

        