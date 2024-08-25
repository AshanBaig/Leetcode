class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=m-1+n-1
        r=m-1
        rem=N-r
        def factorial(num):
            fact=1
            while num:
                fact*=num
                num-=1
            return fact
        N=factorial(N)
        r=factorial(r)
        rem=factorial(rem)
        return int(N/(r*rem))