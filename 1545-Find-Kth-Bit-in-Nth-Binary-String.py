class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert_rev(s):
            sinv=""
            for i in s:
                if i=="1":
                    sinv+="0"
                    continue
                sinv+="1"
            return sinv[::-1]
        a="0"
        for i in range(n-1):
            a=a+"1"+invert_rev(a)
        return a[k-1]