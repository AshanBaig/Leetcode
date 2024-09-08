class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives=0
        while n>0:
            n=int(n//5)
            fives+=n
        return fives