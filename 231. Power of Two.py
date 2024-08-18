class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n!=1 and n%2==1:
            return False
        if n>10:
            r=(len(str(n))-1)*10
        else:
            r=n
        for i in range(r):
            if 2**i==n:
                return True
        return False
        