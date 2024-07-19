class Solution:
    def reverse(self, x: int) -> int:
        if x>=-1*(2**31) and x<=(2**31)-1:
            if x<0:
                ans=-1*int(str(x*-1)[::-1])
            else:
                ans=int(str(x)[::-1])
        if ans>=-1*(2**31) and ans<=(2**31)-1:
            return ans
        else:
            return 0
        